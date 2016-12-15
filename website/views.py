from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from website.event_form import EventForm
from website.forms import UserForm, UserProfileForm
from website.models import Events


def index(request):
    return render(request, 'website/index.html')


def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'website/dashboard.html')
    else:
        return redirect('/')


def profile(request):
    return render(request, 'website/profile.html')


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
        event_obj = Events(event_name=name, description=desc, start_date=s_date, end_date=e_date)

        # saving all the data in the current object into the database
        event_obj.save()

        return render(request, 'website/dashboard.html')

    else:
        form = EventForm()  # an unboundform
        return render(request, 'website/dashboard.html', {'form': form})
