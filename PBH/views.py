from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from .models import Profile
from django.http import JsonResponse
print("hello views")
# instance = Profile.objects.create(name="arman", location="sakinaka",age=21)
# print(instance,"hello check me here")

# def create_profile(request):
#     print("working till here1")
#     if request.method == 'POST':
#         print("hhhhsjadasja")
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form,"form saved")
#             form.save()
#             return redirect('profile_created')
#         print("working till here2")
#     else:
#         print("its in else")
#         form = ProfileForm()
#     return render(request, 'profiles/create_profile.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import ProfileForm


def index(request):
    return render(request, 'NikaahPBH/index.html')


def create_profile(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Form is valid, save the profile
            form.save()
            return redirect('profile_created')
        else:
            # Form is invalid, print errors for debugging
            print(form.errors)
    else:
        # If it's a GET request, create a blank form
        form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})


def profile_created(request):
    return render(request, 'profiles/profile_created.html')



def get_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles.html', {'profiles': profiles})

def contact_us(request):
    # profiles = Profile.objects.all()
    return render(request, 'NikaahPBH/contact_us.html')




def get_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    data = {
        'id': profile.id,
        'name': profile.name,
        'age': profile.age,
        'location': profile.location,
        'profession': profile.profession,
        # Add other fields as needed
    }
    return JsonResponse(data)

from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ProfileForm
from .models import Profile


@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        print("Form Data Received:", request.POST)
        phone_number = request.POST.get('phone_number')
        print("phoen number",phone_number)
        if phone_number is None:
            return JsonResponse({'error': 'Phone number is missing in the request'}, status=400)
        
        # Ensure phone_number is not None before calling strip()
        phone_number = phone_number.strip()
        
        try:
            profile = Profile.objects.get(contact_number=phone_number)
        except Profile.DoesNotExist:
            return JsonResponse({'message': 'No profile found with the provided phone number'}, status=404)
        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Profile updated successfully'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile_update.html', {'form': form})
