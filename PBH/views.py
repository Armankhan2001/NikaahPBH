from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from .models import Profile
from django.http import JsonResponse
print("hello views")
# instance = Profile.objects.create(name="arman", location="sakinaka",age=21)
# print(instance,"hello check me here")

def create_profile(request):
    print("working till here1")
    if request.method == 'POST':
        print("hhhhsjadasja")
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form,"form saved")
            form.save()
            return redirect('profile_created')
        print("working till here2")
    else:
        print("its in else")
        form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})

def profile_created(request):
    return render(request, 'profiles/profile_created.html')



def get_profiles(request):
    profiles = Profile.objects.all()
    data = list(profiles.values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)
# views.py




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

from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def update_profile(request, pk):
    profile = get_object_or_404(Profile, id=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Profile updated successfully'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    return JsonResponse({'message': 'Method not allowed'}, status=405)