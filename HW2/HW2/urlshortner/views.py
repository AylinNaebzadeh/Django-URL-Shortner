from django.shortcuts import render , redirect
import math
from .models import *
from .forms import URLForm
from django.http.request import HttpRequest
from django.http.response import HttpResponseBadRequest, JsonResponse , HttpResponse

class URLGenerator:
    BASE = 62
    UPPERCASE_OFFSET = 55
    LOWERCASE_OFFSET = 61
    DIGIT_OFFSET = 48

    def generate_unique_key(self, integer) -> str:
        """
        Turn an integer [integer] into a base [BASE] number
        in string representation
        """

        # we won't step into the while if integer is 0
        # so we just solve for that case here
        if integer == 0:
            return '0'

        string = ""
        remainder: int = 0
        while integer > 0:
            remainder = integer % self.BASE
            string = self._true_chr(remainder) + string
            integer = int(integer / self.BASE)
        return string

    def get_id(self, key) -> int:
        """
        Turn the base [BASE] number [key] into an integer
        """
        int_sum = 0
        reversed_key = key[::-1]
        for idx, char in enumerate(reversed_key):
            int_sum += self._true_ord(char) * int(math.pow(self.BASE, idx))
        return int_sum

    def _true_ord(self, char):
        """
        Turns a digit [char] in character representation
        from the number system with base [BASE] into an integer.
        """

        if char.isdigit():
            return ord(char) - self.DIGIT_OFFSET
        elif 'A' <= char <= 'Z':
            return ord(char) - self.UPPERCASE_OFFSET
        elif 'a' <= char <= 'z':
            return ord(char) - self.LOWERCASE_OFFSET
        else:
            raise ValueError("%s is not a valid character" % char)

    def _true_chr(self, integer):
        """
        Turns an integer [integer] into digit in base [BASE]
        as a character representation.
        """
        if integer < 10:
            return chr(integer + self.DIGIT_OFFSET)
        elif 10 <= integer <= 35:
            return chr(integer + self.UPPERCASE_OFFSET)
        elif 36 <= integer < 62:
            return chr(integer + self.LOWERCASE_OFFSET)
        else:
            raise ValueError(
                "%d is not a valid integer in the range of base %d" % (integer, BASE))


# Redirect short URL to its original URL, if it's valid
def redirector_view(request):
    form = URLForm()
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            if("http://" not in link) and ("https://" not in link):
                link = "http://" + link
            # uid = 
            new_url_obj = Url(link=link)
            new_url_obj.save()
            id = new_url_obj.pk
            url_generator_obj = URLGenerator()
            sh_url = url_generator_obj.generate_unique_key(id)
            new_url = f"http://127.0.0.1:8000/url/final/{sh_url}"
            json_object = {
                "final_url" : new_url
            }
            return JsonResponse(json_object)
    context = {
        "form" : form
    }
    return HttpResponse(context)

# id = 1024
# generator = URLGenerator()
# key = generator.generate_unique_key(id) # key = GW
# idx = generator.get_id(key)   

def final(request , sh_url):
    url_generator_obj = URLGenerator()
    id = url_generator_obj.get_id(sh_url)
    url_details = Url.objects.get(url_id=id)
    return redirect(url_details.link)



