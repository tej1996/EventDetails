import datetime

import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from website.event_form import EventForm
from website.forms import UserForm, UserProfileForm, BasicProfileForm, CurrentAProfileForm,PreviousAProfileForm,AdditionalProfileForm
from website.models import Event, UserProfile
cloudinary.config(
  cloud_name="tej-mycloud",
  api_key="191512437269526",
  api_secret="s8ETWsWk-Z0N4z_MnPJ4xnWkqPc"
)


def index(request):
    return render(request, 'website/index.html')


def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'website/dashboard.html')
    else:
        return redirect('/')


def profile(request):
    if request.user.is_authenticated():
        return render(request, 'website/profile.html')
    else:
        return redirect('/')


def register(request):

    if not request.user.is_authenticated():

            # A boolean value for telling the template whether the registration was successful.
            # Set to False initially. Code changes value to True when registration succeeds.
            registered = False

            # If it's a HTTP POST, we're interested in processing form data.
            if request.method == 'POST':
                # Attempt to grab information from the raw form information.
                # Note that we make use of both UserForm and UserProfileForm.
                user_form = UserForm(data=request.POST)
                profile_form = UserProfileForm(data=request.POST)

                # If the two forms are valid...
                if user_form.is_valid() and profile_form.is_valid():
                    # Save the user's form data to the database.
                    user = user_form.save()

                    # Now we hash the password with the set_password method.
                    # Once hashed, we can update the user object.
                    user.set_password(user.password)
                    user.save()

                    # Now sort out the UserProfile instance.
                    # Since we need to set the user attribute ourselves, we set commit=False.
                    # This delays saving the model until we're ready to avoid integrity problems.
                    profile = profile_form.save(commit=False)
                    profile.user = user
                    # Now we save the UserProfile model instance.
                    profile.save()

                    # Update our variable to tell the template registration was successful.
                    registered = True

                # Invalid form or forms - mistakes or something else?
                # Print problems to the terminal.
                # They'll also be shown to the user.
                else:
                    print("User Form Errors :" + str(user_form.errors) + "Profile Form Errors" + str(profile_form.errors))

            # Not a HTTP POST, so we render our form using two ModelForm instances.
            # These forms will be blank, ready for user input.
            else:
                user_form = UserForm()
                profile_form = UserProfileForm()

            # Render the template depending on the context.
            return render(request, 'website/index.html', {'user_reg_form': user_form, 'user_profile_form': profile_form,
                                                          'registered': registered})
    else:
            return redirect('/dashboard/')


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username_login')
        password = request.POST.get('pass_login')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect('/dashboard/')
            else:
                # An inactive account was used - no logging in!
                return render(request, 'website/index.html', {'login_error': 'Your account is disabled!'})
        else:
            # Bad login details were provided. So we can't log the user in.
            # print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'website/index.html', {'login_error': 'Invalid Credentials'})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'website/index.html')


def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
    else:
        return redirect('/dashboard/')
    return redirect('/')


def new_event(request):
    if request.method == 'POST':  # if the form has been filled

        form = EventForm(request.POST)

        if form.is_valid():  # All the data is valid
            name = request.POST.get('event_name', '')
            desc = request.POST.get('description', '')
            s_date = request.POST.get('start_date', '')
            e_date = request.POST.get('end_date', '')

        # creating an user object containing all the data
        event_obj = Event(event_name=name, description=desc, start_date=s_date, end_date=e_date)

        # saving all the data in the current object into the database
        event_obj.save()

        return render(request, 'website/dashboard.html')

    else:
        form = EventForm()  # an unboundform
        return render(request, 'website/dashboard.html', {'form': form})


def user_profile(request):

    if request.user.is_authenticated():
        user = get_object_or_404(User, username=request.user.username)
        userprofile = get_object_or_404(UserProfile, user=user)

        user_form = UserForm(instance=user)
        basic_profile_form = BasicProfileForm(instance=userprofile)
        current_profile_form = CurrentAProfileForm(instance=userprofile)
        previous_profile_form = PreviousAProfileForm(instance=userprofile)
        additional_profile_form = AdditionalProfileForm(instance=userprofile)
        message = ""
        upload_error = ""

        if request.POST.get('update') == 'update_basic':
            if request.method == 'POST':
                basic_profile_form = BasicProfileForm(request.POST, request.FILES, instance=userprofile)

                if basic_profile_form.is_valid():

                    if 'passphoto' in request.FILES:
                        if request.FILES['passphoto']:
                            if request.FILES['passphoto'].size <= 300000:
                                p_up_count = userprofile.p_up_count
                                p_up_count += 1
                                if userprofile.passphoto is not None and userprofile.passphoto!="":
                                    cloudinary.uploader.destroy(userprofile.passphoto, invalidate=True, type='authenticated')
                                cloudinary.uploader.upload(request.FILES['passphoto'],
                                                           public_id=user.username + "/passportV" + str(p_up_count),
                                                           type='authenticated')
                                userprofile.passphoto = user.username + "/passportV" + str(p_up_count)
                                userprofile.p_up_count = p_up_count
                            else:
                                upload_error = "File size too large!"
                    if 'sign' in request.FILES:
                        if request.FILES['sign']:
                            if request.FILES['sign'].size <= 300000:
                                s_up_count = userprofile.s_up_count
                                s_up_count += 1
                                if userprofile.sign is not None and userprofile.sign != "":
                                    cloudinary.uploader.destroy(userprofile.sign, invalidate=True, type='authenticated')
                                cloudinary.uploader.upload(request.FILES['sign'],
                                                           public_id=user.username + "/signV" + str(s_up_count),
                                                           type='authenticated')
                                userprofile.sign = user.username + "/signV" + str(s_up_count)
                                userprofile.s_up_count = s_up_count
                            else:
                                upload_error = "File size too large!"
                    userprofile = basic_profile_form.save()
                    userprofile.age = int((datetime.date.today() - userprofile.dob).days / 365.25)
                    userprofile.save()
                    message = 'Successfully Updated!'
                else:
                    print("Profile Form Errors" + str(basic_profile_form.errors))
        else:
            if request.POST.get('update') == 'update_current':
                if request.method == 'POST':
                    current_profile_form = CurrentAProfileForm(data=request.POST, instance=userprofile)

                    if current_profile_form.is_valid():
                        userprofile = current_profile_form.save()
                        userprofile.save()
                        message = 'Successfully Updated!'
                    else:
                        print("Profile Form Errors" + str(current_profile_form.errors))
            else:
                if request.POST.get('update') == 'update_previous':
                    if request.method == 'POST':
                        previous_profile_form = PreviousAProfileForm(data=request.POST, instance=userprofile)

                        if previous_profile_form.is_valid():
                            userprofile = previous_profile_form.save()
                            userprofile.save()
                            message = 'Successfully Updated!'
                        else:
                            print("Profile Form Errors" + str(previous_profile_form.errors))
                else:
                    if request.POST.get('update') == 'update_additional':
                        if request.method == 'POST':
                            additional_profile_form = AdditionalProfileForm(data=request.POST, instance=userprofile)

                            if additional_profile_form.is_valid():
                                userprofile = additional_profile_form.save()
                                userprofile.save()
                                message = 'Successfully Updated!'
                            else:
                                print("Profile Form Errors" + str(additional_profile_form.errors))
                    else:
                        message = ""
        currpassphoto = cloudinary.CloudinaryImage(userprofile.passphoto).image(sign_url=True, width=0.5,
                                                                                type='authenticated')
        sign = cloudinary.CloudinaryImage(userprofile.sign).image(sign_url=True, width=0.3, type='authenticated')
        return render(request, 'website/profile.html', {'message:': message,
                                                        'user_form': user_form,
                                                        'basic_profile_form': basic_profile_form,
                                                        'current_profile_form': current_profile_form,
                                                        'previous_profile_form': previous_profile_form,
                                                        'additional_profile_form': additional_profile_form,
                                                        'currpassphoto': currpassphoto,
                                                        'sign': sign,
                                                        'upload_error': upload_error})
    else:
        return redirect('/')
