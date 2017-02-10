from django import forms
from django.contrib.auth.models import User
from django.forms.extras import SelectDateWidget
from datetime import datetime

from website.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password',
                                                                 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username',
                                               'id': 'InputUser_reg', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email',
                                             'id': 'InputEmail_reg', 'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The Email Id Already Exists!")
        return email


class UserProfileForm(forms.ModelForm):
    CHOICES = [('0', 'Student'),
               ('1', 'Faculty')]
    type = forms.ChoiceField(choices=CHOICES, widget=forms.Select)

    class Meta:
        model = UserProfile
        fields = ('name', 'type',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name',
                                           'id': 'InputUser_userProfile', 'class': 'form-control'}),
        }


class BasicProfileForm(forms.ModelForm):

    CHOICES = [('M', 'Male'),
               ('F', 'Female')]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    dob = forms.DateField(widget=SelectDateWidget(years=range(1980, 2017)))

    class Meta:
        model = UserProfile
        fields = ('name', 'dob', 'gender', 'birthplace', 'contact', 'alternate_contact',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name',
                                           'id': 'form-name', 'class': 'form-control'}),

            'birthplace': forms.TextInput(attrs={'placeholder': 'Enter Birth Place',
                                                 'id': 'form-birthplace', 'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter Contact No.',
                                              'id': 'form-contact', 'class': 'form-control'}),
            'alternate_contact': forms.TextInput(attrs={'placeholder': 'Enter Alternate Contact No.',
                                                        'id': 'form-acontact', 'class': 'form-control'}),
        }


class CurrentAProfileForm(forms.ModelForm):
    CHOICES_SEM = [('', 'Select Current Semester'),
                   ('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'),
                   ('8', 'VIII')]
    semester = forms.ChoiceField(choices=CHOICES_SEM, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    CHOICES_YEAR = [('', 'Select Current Year'), ('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV')]
    year = forms.ChoiceField(choices=CHOICES_YEAR, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    CHOICES_BRANCH = [('', 'Select Branch'), ('CSE', 'Computer Science'), ('EC', 'Electronics & Comm.'),
                      ('EE', 'Electrical & Electronics Comm.'), ('IT', 'Information & Technology'),
                      ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering')]
    branch = forms.ChoiceField(choices=CHOICES_BRANCH, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('class_rno', 'univ_rno', 'semester', 'section', 'batch', 'year', 'branch', 'college',
                  'per_sem1', 'per_sem2', 'per_sem3', 'per_sem4', 'per_sem5', 'per_sem6', 'per_sem7', 'per_sem8',)
        widgets = {
            'class_rno': forms.TextInput(attrs={'placeholder': 'Class Roll No.', 'class': 'form-control'}),
            'univ_rno': forms.TextInput(attrs={'placeholder': 'University Roll No.', 'class': 'form-control'}),
            'section': forms.TextInput(attrs={'placeholder': 'Section', 'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'placeholder': 'Batch', 'class': 'form-control'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name', 'class': 'form-control'}),
            'per_sem1': forms.TextInput(attrs={'placeholder': 'I Sem Percentage', 'class': 'form-control'}),
            'per_sem2': forms.TextInput(attrs={'placeholder': 'II Sem Percentage', 'class': 'form-control'}),
            'per_sem3': forms.TextInput(attrs={'placeholder': 'III Sem Percentage', 'class': 'form-control'}),
            'per_sem4': forms.TextInput(attrs={'placeholder': 'IV Sem Percentage', 'class': 'form-control'}),
            'per_sem5': forms.TextInput(attrs={'placeholder': 'V Sem Percentage', 'class': 'form-control'}),
            'per_sem6': forms.TextInput(attrs={'placeholder': 'VI Sem Percentage', 'class': 'form-control'}),
            'per_sem7': forms.TextInput(attrs={'placeholder': 'VII Sem Percentage', 'class': 'form-control'}),
            'per_sem8': forms.TextInput(attrs={'placeholder': 'VIII Sem Percentage', 'class': 'form-control'}),
        }


class PreviousAProfileForm(forms.ModelForm):
    CHOICES_MEDIUM = [('', 'Select Medium'), ('E', 'English'), ('H', 'Hindi')]
    medium_twelfth = forms.ChoiceField(choices=CHOICES_MEDIUM, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    medium_tenth = forms.ChoiceField(choices=CHOICES_MEDIUM, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('admission_mode', 'admission_rank',
                  'percentage_tenth', 'board_tenth', 'medium_tenth', 'year_tenth', 'school_tenth',
                  'percentage_twelfth', 'board_twelfth', 'medium_twelfth', 'year_twelfth', 'school_twelfth',
                  'percentage_diploma', 'stream_diploma', 'year_diploma', 'college_diploma',)
        widgets = {
            'admission_mode': forms.TextInput(attrs={'placeholder': 'Admission Mode', 'class': 'form-control'}),
            'admission_rank': forms.TextInput(attrs={'placeholder': 'Admission Rank (RPET/AIEEE)', 'class': 'form-control'}),
            'percentage_tenth': forms.TextInput(attrs={'placeholder': '10th Percentage', 'class': 'form-control'}),
            'board_tenth': forms.TextInput(attrs={'placeholder': 'Board(Eg.CBSE,RBSE)', 'class': 'form-control'}),
            'year_tenth': forms.TextInput(attrs={'placeholder': 'Year of Passing', 'class': 'form-control'}),
            'school_tenth': forms.TextInput(attrs={'placeholder': 'School Name', 'class': 'form-control'}),
            'percentage_twelfth': forms.TextInput(attrs={'placeholder': '12th Percentage', 'class': 'form-control'}),
            'board_twelfth': forms.TextInput(attrs={'placeholder': 'Board(Eg.CBSE,RBSE)', 'class': 'form-control'}),
            'year_twelfth': forms.TextInput(attrs={'placeholder': 'Year of Passing', 'class': 'form-control'}),
            'school_twelfth': forms.TextInput(attrs={'placeholder': 'School Name', 'class': 'form-control'}),
            'percentage_diploma': forms.TextInput(attrs={'placeholder': 'Diploma Percentage', 'class': 'form-control'}),
            'stream_diploma': forms.TextInput(attrs={'placeholder': 'Stream in which Diploma done', 'class': 'form-control'}),
            'year_diploma': forms.TextInput(attrs={'placeholder': 'Year of Passing', 'class': 'form-control'}),
            'college_diploma': forms.TextInput(attrs={'placeholder': 'College Name (Diploma)', 'class': 'form-control'}),
        }


class AdditionalProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('father_name', 'father_contact', 'father_occupation', 'mother_name', 'mother_contact', 'mother_occupation',
                  'guardian_contact', 'present_address', 'permanent_address', )
        widgets = {
            'father_name': forms.TextInput(attrs={'placeholder': "Father's Name", 'class': 'form-control'}),
            'father_contact': forms.TextInput(attrs={'placeholder': "Father's Contact", 'class': 'form-control'}),
            'father_occupation': forms.TextInput(attrs={'placeholder': "Father's Occupation", 'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'placeholder': "Mother's Name", 'class': 'form-control'}),
            'mother_contact': forms.TextInput(attrs={'placeholder': "Mother's Contact", 'class': 'form-control'}),
            'mother_occupation': forms.TextInput(attrs={'placeholder': "Mother's Occupation", 'class': 'form-control'}),
            'guardian_contact': forms.TextInput(attrs={'placeholder': "Guardian's Contact", 'class': 'form-control'}),
            'present_address': forms.Textarea(attrs={'placeholder': "Present Address", 'class': 'form-control'}),
            'permanent_address': forms.Textarea(attrs={'placeholder': "Permanent Address", 'class': 'form-control'}),
        }
