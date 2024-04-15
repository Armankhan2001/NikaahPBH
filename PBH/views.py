
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm,ProfileFormDesc
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'NikaahPBH/index.html')

def dark_mode(request):
    return render(request, 'profiles/dark_mode.html')



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
    # Retrieve the latest profile instance created
    latest_profile = Profile.objects.latest('id')
    return render(request, 'profiles/profile_created.html', {'profile': latest_profile})





def get_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles.html', {'profiles': profiles})

def contact_us(request):
    # profiles = Profile.objects.all()
    return render(request, 'NikaahPBH/contact_us.html')




def get_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    data = {
        'image':profile.image,
        'name': profile.name,
        'age': profile.age,
        'gender': profile.gender,
        'location': profile.location,
        'profession': profile.profession,
        'contact_number': profile.contact_number,
        'instagram_id': profile.instagram_id,
        # Add other fields as needed
        'introduction':profile.introduction,
        'image1':profile.image1,
        'image2':profile.image1,
        'image3':profile.image1,
        'message':profile.message,
        'gmail_id':profile.gmail_id,
        'dob':profile.dob,
        'education':profile.education,
        'native_place':profile.native_place,
        'current_living_in':profile.current_living_in,
        'religion':profile.religion,
        'mother_occupation':profile.mother_occupation,
        'father_occupation':profile.father_occupation
    }
       
    return render(request, 'profiles/profile.html', {'profile': data,})




@csrf_exempt
def update_profile(request):
    print("chrck")
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if phone_number is None:
            return JsonResponse({'error': 'Phone number is missing in the request'}, status=400)
        print("none p no")
        
        # Ensure phone_number is not None before calling strip()
        phone_number = phone_number.strip()
        try:
            profile = Profile.objects.get(contact_number=phone_number)
            print("noooooooo")
        except Profile.DoesNotExist:
            return JsonResponse({'message': 'No profile found with the provided phone number'}, status=404)
        print("noookkakakk")
        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            print("kakakakkkka")
            return JsonResponse({'message': 'Profile updated successfully'})
        else:
            print("else em")
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        print("else last one")
        form = ProfileForm()
    return render(request, 'profiles/profile_update.html', {'form': form})





def delete_profile(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if not phone_number:
            return JsonResponse({'error': 'Phone number is missing in the request'}, status=400)
        
        # Ensure phone_number is not None before calling strip()
        phone_number = phone_number.strip()
        
        try:
            # Attempt to fetch the profile based on the phone number
            profile = Profile.objects.get(contact_number=phone_number)
            # Delete the profile
            profile.delete()
            return JsonResponse({'message': 'Profile deleted successfully'})
        except Profile.DoesNotExist:
            # If no profile exists with the provided phone number
            return JsonResponse({'message': 'No profile found with the provided phone number'}, status=404)
    else:
        # If it's not a POST request, render the template with an empty form
        return render(request, 'profiles/delete_profile.html')

        





def back(request):
    # Get the previous URL from the session, or default to '/'
    previous_url = request.session.get('previous_url', '/')
    # Redirect to the previous URL
    return redirect(previous_url)





@csrf_exempt
def profile_desc(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if not phone_number:
            return JsonResponse({'error': 'Phone number is missing in the request'}, status=400)
        
        phone_number = phone_number.strip()
        
        try:
            profile = Profile.objects.get(contact_number=phone_number)
        except Profile.DoesNotExist:
            return JsonResponse({'message': 'No profile found with the provided phone number'}, status=404)
        
        form = ProfileFormDesc(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            print(":pro saved")
            print("profile_id =",profile.id)
            return redirect('profiledesc_created', profile_id=profile.id)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = ProfileFormDesc()
        return render(request, 'profiles/addprofiledesc.html', {'form': form})


def profiledesc_created(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    return render(request, 'profiles/profiledesc_created.html', {'profile': profile})