from django.shortcuts import redirect
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import timedelta

class CheckUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Ensure you have the correct `uidb64` and `token`
        uidb64 = "example_uidb64"  # Replace with the actual UID in base64 format
        token = "example_token"  # Replace with the actual token

        # List of exempt URLs that don't require the user to be logged in
        exempt_urls = [
            reverse('login'),  # Regular login page
            reverse('logout'),  # Regular logout page
            reverse('password_reset'),  # Password reset page
            reverse('password_reset_done'),  # After password reset request
            reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token}),  # Password reset confirmation
            reverse('password_reset_complete'),  # Password reset complete
        ]

        # Skip authentication checks for exempt URLs
        if request.path.startswith('/admin') or any(request.path.startswith(url) for url in exempt_urls):
            return self.get_response(request)

        if request.user.is_authenticated:
            # Check if the user's account is active
            if not request.user.is_active:
                return redirect('account_locked')  # Redirect to account locked page if inactive

            # Password expiration check (if a custom expiration logic is required)
            if self.is_password_expired(request.user):
                return redirect('password_change')  # Redirect to password change if expired

        else:
            # Redirect unauthenticated users to the login page
            return redirect('login')  # Change this to your login URL if needed

        # Process the request if the user is authenticated and meets all checks
        response = self.get_response(request)
        return response

    def is_password_expired(self, user):
        """
        Custom function to check if the user's password has expired.
        You can customize this logic based on your requirements.
        For example, if the password expiration date is stored in a custom user model field.
        """
        expiration_date = getattr(user, 'password_changed_at', None)  # Assuming password change time is tracked
        if expiration_date:
            # Define password expiration period (e.g., 90 days)
            expiration_period = timedelta(days=90)
            if now() - expiration_date > expiration_period:
                return True
        return False
