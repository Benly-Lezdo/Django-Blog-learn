from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, Category, Contact
from django.core.paginator import Paginator
from .forms import ContactForm

# static demo data
# post = [
#     {
#         "id": 1,
#         "title": "Post Title",
#         "content": "Lorem Ipsum is simply dummy text of the printing",
#         "url": "https://static.vecteezy.com/system/resources/previews/033/919/308/non_2x/the-sun-rises-over-the-mountains-and-flowers-in-the-foreground-ai-generated-free-photo.jpg",
#     },
#     {
#         "id": 2,
#         "title": "Header",
#         "content": "typesetting industry. Lorem Ipsum",
#         "url": "https://cdn.pixabay.com/photo/2021/08/25/20/42/field-6574455_640.jpg",
#     },
#     {
#         "id": 3,
#         "title": "Body",
#         "content": "when an unknown printer took a galley of type and scrambled",
#         "url": "https://media.istockphoto.com/id/803859390/photo/farm-landscape.jpg?s=612x612&w=0&k=20&c=kJqtSV9IWeOcDU89sFoRpoAJgDmquimTS3up8W4-s7o=",
#     },
#     {
#         "id": 4,
#         "title": "Middle order",
#         "content": "Many desktop publishing packages and web page",
#         "url": "https://iso.500px.com/wp-content/uploads/2018/05/Blog-marketplace-getty500px-48429366-nologo-3000x2000.png",
#     },
# ]


# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    # getting data from post model
    all_post = Post.objects.all()

    # pagination
    paginator = Paginator(all_post, 5)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    category = Category.objects.all()
    return render(
        request,
        "index.html",
        {"title": blog_title, "posts": page_object, "category_data": category},
    )


def detail(request, slug):
    # print(post_id)
    # getting static data
    # getpost = next((item for item in post if item["id"] == post_id), None)
    # print(getpost)

    # getting data from modal post id
    try:
        getpost = Post.objects.get(slug=slug)
        related_post = Post.objects.filter(category_id=getpost.category_id).exclude(
            pk=getpost.id
        )
    except Post.DoesNotExist:
        return HttpResponse("Post not found", status=404)

    blog_title = "mmbu"
    logger = logging.getLogger()
    # logger.debug(f"post variable is {getpost}")
    return render(
        request,
        "detail.html",
        {"tits": blog_title, "getpost": getpost, "related_posts": related_post},
    )


def oldUrl(request):
    return redirect(reverse("blog:newUrlTest"))


def newUrl(request):
    test = "mmbu"
    age = 12
    return HttpResponse(f"This is the new url {test} and age is {age}")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        logger = logging.getLogger()
        if form.is_valid():
            # Check if the email already exists
            if Contact.objects.filter(email=email).exists():
                error_message = "Email already exists"

                logger.debug(f"Email already exists: {email}")
                return render(
                    request,
                    "contact.html",
                    {
                        "form": form,
                        "error_message": error_message,
                        "name": name,
                        "email": email,
                        "message": message,
                    },
                )

            # Create and save the Contact instance to the database
            contact = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
            )
            contact.save()

            logger.debug(f"Post data is {form.cleaned_data['name']}")
            success_message = "Your email has been sent"

            return render(
                request,
                "contact.html",
                {
                    "form": form,
                    "success_message": success_message,
                },
            )
        else:
            logger.debug("Form validation failure")
            return render(
                request,
                "contact.html",
                {"form": form, "name": name, "email": email, "message": message},
            )
    return render(request, "contact.html")


def about_page(request):
    return render(request, "about.html")
