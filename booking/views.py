from django.shortcuts import render,get_object_or_404

# Create your views here.

# def home(req):
#     return  render(req,'home.html')

# def about(request):
#     return render(request,'about.html')

# def contact(request):
#     return  render(request,'contact.html')


# def welcome(request):
#     return  render(request,'welcome.html')


# from .models import BloodInfo
# def register(request):
#         if request.method == 'POST':
#             # Get form data
#             name = request.POST.get('name')
#             password = request.POST.get('password')
#             phono = request.POST.get('phono')
#             email = request.POST.get('email')
#             blood_group = request.POST.get('blood_group')
#             address = request.POST.get('address')

#             # Save data to the database
#             res=BloodInfo.objects.create(
#                 name=name,
#                 password=password,
#                 phono=phono,
#                 email=email,
#                 blood_group=blood_group,
#                 address=address
#             )
#             res.save()
#             return render(request,'register.html')
#         else:
#             return render(request,'register.html')


# from .models import BloodInfo # Assuming you have a User model

# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")


#         try:
#             res = BloodInfo.objects.get(name=username, password=password)

#             return render(request, "welcome.html", {'res': res})
#         except BloodInfo.DoesNotExist:

#             return render(request, "login.html", {"error": "Invalid username or password"})


#     return render(request, "login.html")



# from .models import BloodInfo
# def display(request):
#     # Get all records from BloodInfo
#     all_data = BloodInfo.objects.all()
#     return render(request, "display.html", {"data": all_data})


# def logout(request):
#     return render(request,'logout.html')


# from .models import BloodInfo

# def update(request):
#     donor = None
#     message = ""

#     if request.method == "POST":
#         if "search" in request.POST:
#             donor_id = request.POST.get("donor_id")
#             try:
#                 donor = BloodInfo.objects.get(id=donor_id)
#             except BloodInfo.DoesNotExist:
#                 message = "❌ Donor not found!"

#         elif "update" in request.POST:
#             donor_id = request.POST.get("donor_id")
#             donor = get_object_or_404(BloodInfo, id=donor_id)

#             donor.name = request.POST.get("name")
#             donor.phone = request.POST.get("phone")
#             donor.address = request.POST.get("address")
#             donor.save()

#             message = "✅ Donor details updated successfully!"

#     return render(request, "update.html", {"donor": donor, "message": message})



# from .models import BloodInfo

# def delete(request):
#     donor = None
#     message = ""

#     if request.method == "POST":
#         donor_id = request.POST.get("donor_id")

#         if "search" in request.POST:
#             try:
#                 donor = BloodInfo.objects.get(id=donor_id)
#             except BloodInfo.DoesNotExist:
#                 message = "❌ Donor not found."

#         elif "delete" in request.POST:
#             try:
#                 donor = BloodInfo.objects.get(id=donor_id)
#                 donor.delete()
#                 message = "✅ Donor deleted successfully!"
#             except BloodInfo.DoesNotExist:
#                 message = "❌ Donor not found."

#     return render(request, "delete.html", {"donor": donor, "message": message})



# from .models import BloodInfo

# def search(request):
#     donors = None
#     message = ""

#     if request.method == "POST":
#         blood_group = request.POST.get("blood_group")

#         # Search for donors with that blood group
#         donors = BloodInfo.objects.filter(blood_group__iexact=blood_group)

#         if not donors.exists():
#             message = f"No donors found with blood group {blood_group}"

#     return render(request, "search.html", {"donors": donors, "message": message})


###update code here----------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.

def home(req):
    return  render(req,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return  render(request,'contact.html')

#
# def welcome(request):
#     return  render(request,'welcome.html')

def welcome(request):
    # Check if user is logged in (session exists)
    if not request.session.get('user_id'):
        # If no session → redirect to login page
        return redirect('login')

    # Get user name from session to display on page
    user_name = request.session.get('user_name')
    return render(request, 'welcome.html', {'user_name': user_name})

from .models import BloodInfo
def register(request):
        if request.method == 'POST':
            # Get form data
            name = request.POST.get('name')
            password = request.POST.get('password')
            phono = request.POST.get('phono')
            email = request.POST.get('email')
            blood_group = request.POST.get('blood_group')
            address = request.POST.get('address')

            # Save data to the database
            res=BloodInfo.objects.create(
                name=name,
                password=password,
                phono=phono,
                email=email,
                blood_group=blood_group,
                address=address
            )
            res.save()
            return render(request,'register.html',{'msg':'Register successful! '})
        else:
            return render(request,'register.html')



# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#
#         try:
#             res = BloodInfo.objects.get(name=username, password=password)
#
#             return render(request, "welcome.html", {'res': res})
#         except BloodInfo.DoesNotExist:
#
#             return render(request, "login.html", {"error": "Invalid username or password"})
#
#
#     return render(request, "login.html")
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            res = BloodInfo.objects.get(name=username, password=password)

            # ✅ Store user info in session
            request.session['user_id'] = res.id
            request.session['user_name'] = res.name

            return redirect('welcome')  # redirect to welcome page
        except BloodInfo.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid username or password"})

    # ✅ If already logged in, skip login page
    if request.session.get('user_id'):
        return redirect('welcome')

    return render(request, "login.html")




from .models import BloodInfo
def display(request):
    # Get all records from BloodInfo
    all_data = BloodInfo.objects.all()
    return render(request, "display.html", {"data": all_data})


# def logout(request):
#     return render(request,'logout.html')

def logout(request):
    # Clear all session data
    request.session.flush()
    # Redirect to login page
    return redirect('login')

from .models import BloodInfo

def update(request):
    donor = None
    message = ""

    if request.method == "POST":
        if "search" in request.POST:
            donor_id = request.POST.get("donor_id")
            try:
                donor = BloodInfo.objects.get(id=donor_id)
            except BloodInfo.DoesNotExist:
                message = "❌ Donor not found!"

        elif "update" in request.POST:
            donor_id = request.POST.get("donor_id")
            donor = get_object_or_404(BloodInfo, id=donor_id)

            donor.name = request.POST.get("name")
            donor.phone = request.POST.get("phone")
            donor.address = request.POST.get("address")
            donor.save()

            message = "✅ Donor details updated successfully!"

    return render(request, "update.html", {"donor": donor, "message": message})



from .models import BloodInfo

# def delete(request):
#     donor = None
#     message = ""
#
#     if request.method == "POST":
#         donor_id = request.POST.get("donor_id")
#
#         if "search" in request.POST:
#             try:
#                 donor = BloodInfo.objects.get(id=donor_id)
#             except BloodInfo.DoesNotExist:
#                 message = "❌ Donor not found."
#
#         elif "delete" in request.POST:
#             try:
#                 donor = BloodInfo.objects.get(id=donor_id)
#                 donor.delete()
#                 message = "✅ Donor deleted successfully!"
#             except BloodInfo.DoesNotExist:
#                 message = "❌ Donor not found."
#
#     return render(request, "delete.html", {"donor": donor, "message": message})

def delete(request):
    donor = None
    message = ""
    MASTER_KEY = "1234"  # You can change this to your secret key

    if request.method == "POST":
        donor_id = request.POST.get("donor_id")
        entered_key = request.POST.get("master_key")

        # Step 1: Check if key is correct
        if entered_key != MASTER_KEY:
            message = "🚫 Invalid master key. You cannot delete records."
            return render(request, "delete.html", {"message": message})

        # Step 2: Continue only if key correct
        if "search" in request.POST:
            try:
                donor = BloodInfo.objects.get(id=donor_id)
            except BloodInfo.DoesNotExist:
                message = "❌ Donor not found."

        elif "delete" in request.POST:
            try:
                donor = BloodInfo.objects.get(id=donor_id)
                donor.delete()
                message = "✅ Donor deleted successfully!"
            except BloodInfo.DoesNotExist:
                message = "❌ Donor not found."

    return render(request, "delete.html", {"donor": donor, "message": message})


from .models import BloodInfo

def search(request):
    donors = None
    message = ""

    if request.method == "POST":
        blood_group = request.POST.get("blood_group")

        # Search for donors with that blood group
        donors = BloodInfo.objects.filter(blood_group__iexact=blood_group)

        if not donors.exists():
            message = f"No donors found with blood group {blood_group}"

    return render(request, "search.html", {"donors": donors, "message": message})


