from django.conf import settings
import requests

class CaptchaValidator:
    
    def validate_captcha(self, captcha_response):
        if not captcha_response:
            return False, "Captcha response is required"
        
        payload = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        result = response.json()
        if not result.get('success', False):
            return False, "Captcha validation failed"
        
        return True, "Captcha validation successful"