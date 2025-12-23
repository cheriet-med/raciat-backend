from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)  # Add using=self._db here
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_phone_number_verified = models.BooleanField(default=False)
    premium_plan = models.BooleanField(default=False)
    full_name = models.CharField(max_length=1000, blank=True, null=True)
    address_line_1 = models.CharField(max_length=1000, blank=True, null=True)
    address_line_2 = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    postalCode = models.CharField(max_length=1000, blank=True, null=True)
    countryCode = models.CharField(max_length=1000, blank=True, null=True)
    phoneNumber = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True)
    username = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    identity_verified = models.BooleanField(default=False)
    location = models.CharField(max_length=1000, blank=True, null=True)
    plan = models.CharField(max_length=1000, blank=True, null=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    pets = models.CharField(max_length=1000, blank=True, null=True)
    born = models.CharField(max_length=1000, blank=True, null=True)
    time_spend = models.CharField(max_length=1000, blank=True, null=True)
    want_to_go = models.CharField(max_length=1000, blank=True, null=True)
    obsessed = models.CharField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)
    language = models.CharField(max_length=1000, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longtitude = models.FloatField(blank=True, null=True) 
    joined = models.CharField(max_length=1000, blank=True, null=True)
    types = models.CharField(max_length=1000, blank=True, null=True)
    stars = models.CharField(max_length=1000, blank=True, null=True)



    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.full_name

 
    
    def __str__(self):
        return self.email
        









class Languages(models.Model):

    user = models.ForeignKey(UserAccount, related_name='Languages', on_delete=models.CASCADE)
    language = models.CharField(max_length=1000, blank=True, null=True)
  
    def __str__(self):
        return self.language



class Verify(models.Model):
    user = models.ForeignKey(UserAccount, related_name='verification', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000,blank=True, null=True)
    document_type = models.CharField(max_length=500,blank=True, null=True)
    document_number = models.CharField(max_length=500,blank=True, null=True)
    document_photo = models.ImageField(blank=True, null=True)
    selfie_document = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=500,blank=True, null=True, default='unverified')
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.email






class NewsLetter(models.Model):
    email = models.CharField(max_length=1000,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.email


class EmailLetter(models.Model):
    first_name = models.CharField(max_length=1000,blank=True, null=True)
    last_name = models.CharField(max_length=1000,blank=True, null=True)
    company = models.CharField(max_length=1000,blank=True, null=True)
    email = models.CharField(max_length=1000,blank=True, null=True)
    message = models.CharField(max_length=1000,blank=True, null=True)
    full_name = models.CharField(max_length=500,blank=True, null=True)
    is_read = models.BooleanField(default=False)
    subject = models.CharField(max_length=500,blank=True, null=True)
    category = models.CharField(max_length=500,blank=True, null=True)
    message_type = models.CharField(max_length=500,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)

    
    def __str__(self):
        return self.email



class Post(models.Model):
    user = models.ForeignKey(UserAccount, related_name='Blog', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=1000,blank=True, null=True)
    description = models.CharField(max_length=1000,blank=True, null=True)
    content = models.CharField(max_length=10000,blank=True, null=True)
    category = models.CharField(max_length=10000,blank=True, null=True)
    image_owner = models.CharField(max_length=10000,blank=True, null=True)
    owner = models.CharField(max_length=1000,blank=True, null=True)
    created_at_meta = models.CharField(max_length=50, blank=True)
    updated_at_meta = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        now = timezone.now().isoformat()
        if not self.created_at_meta:
            self.created_at_meta = now
        self.updated_at_meta = now
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en


# for Listings


class Product(models.Model):
    user = models.ForeignKey(UserAccount, related_name='Listings', on_delete=models.CASCADE)
    name = models.CharField(max_length=1000,blank=True, null=True)
    description = models.CharField(max_length=50000,blank=True, null=True)
    category = models.CharField(max_length=1000,blank=True, null=True)
    types = models.CharField(max_length=1000,blank=True, null=True)
    price = models.CharField(max_length=1000,blank=True, null=True)
    currency = models.CharField(max_length=1000,blank=True, null=True)
    video_link = models.CharField(max_length=1000,blank=True, null=True)
    rooms_number = models.CharField(max_length=1000,blank=True, null=True)
    badrooms_number = models.CharField(max_length=1000,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    latitude = models.CharField(max_length=1000, blank=True, null=True)
    longtitude = models.CharField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    created_at_meta = models.CharField(max_length=50, blank=True)
    updated_at_meta = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=1000,blank=True, null=True)
    capacity = models.CharField(max_length=1000,blank=True, null=True)
    established = models.CharField(max_length=1000,blank=True, null=True)
    garages = models.CharField(max_length=1000,blank=True, null=True)
    region = models.CharField(max_length=1000,blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)



    def save(self, *args, **kwargs):
        now = timezone.now().isoformat()
        if not self.created_at_meta:
            self.created_at_meta = now
        self.updated_at_meta = now
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name



class Amenities(models.Model):

    product = models.ForeignKey(Product, related_name='Amenities', on_delete=models.CASCADE, null=True, blank=True)
    amenitie = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    categoty = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image =  models.ImageField(blank=True, null=True)
    #is_primary = models.BooleanField(default=False)  # To mark the primary image for the product

    def __str__(self):
        return f"Image for {self.product.name}"





class Nearbyattractions(models.Model):
    product = models.ForeignKey(Product, related_name='nearby_attractions', on_delete=models.CASCADE)
    name =  models.CharField(max_length=1000,blank=True, null=True)
    distance =  models.CharField(max_length=1000,blank=True, null=True)

    def __str__(self):
        return f"Distance for {self.product.name}"




class Awards(models.Model):
    product = models.ForeignKey(Product, related_name='awards', on_delete=models.CASCADE)
    rooms =  models.CharField(max_length=1000,blank=True, null=True)
    badrbadroomes =  models.CharField(max_length=1000,blank=True, null=True)
    image =  models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"Awards for {self.product.name}"


class Specialties(models.Model):
    product = models.ForeignKey(Product, related_name='specialties', on_delete=models.CASCADE)
    specialties =  models.CharField(max_length=1000,blank=True, null=True)

    def __str__(self):
        return f"Specialties for {self.product.name}"



class SendEmailForPassword(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    email = models.CharField(max_length=500,blank=True, null=True)
    password = models.CharField(max_length=500,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"{self.name}"




class Wishlist(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlisted_by")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")  # prevent duplicates

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"




class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, related_name='reviews', on_delete=models.CASCADE)
    rating_global = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    room = models.CharField(max_length=1000, blank=True, null=True)
    restaurant_space = models.CharField(max_length=1000, blank=True, null=True)
    value = models.CharField(max_length=1000, blank=True, null=True)
    clearliness = models.CharField(max_length=1000, blank=True, null=True)
    service = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    updated_at = models.CharField(max_length=1000, blank=True, null=True)
    stay_date = models.CharField(max_length=1000, blank=True, null=True)
    trip_type = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"Review by {self.UserAccount.email} for {self.product.title_en}"

    class Meta:
        unique_together = ('product', 'user')  # Ensure a user can only review a product once





class RviewsImage(models.Model):
    ProductReview = models.ForeignKey(ProductReview, related_name='Reviews_image', on_delete=models.CASCADE)
    image =  models.ImageField(blank=True, null=True)
    #is_primary = models.BooleanField(default=False)  # To mark the primary image for the product

    def __str__(self):
        return f"Image for {self.RviewsImage.comment}"




class ReviewHelpful(models.Model):
    review = models.ForeignKey(ProductReview, related_name="helpful_votes", on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, related_name='user_reviews_vote', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("review", "user")  # one vote per user


class ReviewReport(models.Model):
    review = models.ForeignKey(ProductReview, related_name="reports", on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, related_name='user_reviews_raports', on_delete=models.CASCADE)
    reason = models.CharField(max_length=1000, blank=True, null=True)
    informations = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("review", "user")  # one report per user



class ReviewScore(models.Model):
    product = models.ForeignKey(Product, related_name="score", on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, related_name='user_reviews_score', on_delete=models.CASCADE)
    clean = models.CharField(max_length=1000, blank=True, null=True)
    blur = models.CharField(max_length=1000, blank=True, null=True)
    verified = models.CharField(max_length=1000, blank=True, null=True)
    fake = models.CharField(max_length=1000, blank=True, null=True)
    total = models.CharField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return f"{self.user}"




class Order(models.Model):

    user = models.ForeignKey(UserAccount, related_name='user_orders', on_delete=models.CASCADE)
    name = models.CharField(max_length=500,blank=True, null=True)
    status = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.CharField(max_length=500,blank=True, null=True)
    updated_at = models.CharField(max_length=500,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=500,blank=True, null=True)
    reason = models.CharField(max_length=500,blank=True, null=True)
    price = models.CharField(max_length=500,blank=True, null=True)
    types = models.CharField(max_length=500,blank=True, null=True)
    hurry = models.CharField(max_length=500,blank=True, null=True)
    surface = models.CharField(max_length=500,blank=True, null=True)
    latitude = models.CharField(max_length=1000, blank=True, null=True)
    longtitude = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=500,blank=True, null=True)
    representative = models.CharField(max_length=500,blank=True, null=True)
    potential_client = models.CharField(max_length=500,blank=True, null=True)
    types = models.CharField(max_length=500,blank=True, null=True)
    min_price = models.CharField(max_length=500,blank=True, null=True)
    max_price = models.CharField(max_length=500,blank=True, null=True)
    badrooms_number = models.CharField(max_length=500,blank=True, null=True)
    rooms_number = models.CharField(max_length=500,blank=True, null=True)
    region = models.CharField(max_length=500,blank=True, null=True)
    location = models.CharField(max_length=500,blank=True, null=True)
    is_read = models.BooleanField(default=False)
    phone = models.CharField(max_length=500,blank=True, null=True)
    responsable = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id}"






class SendEmailCreateOrder(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    email = models.CharField(max_length=500,blank=True, null=True)
    OrderID = models.CharField(max_length=500,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date_time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"{self.name}"





class SendEmailTrakingNumber(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    email = models.CharField(max_length=500,blank=True, null=True)
    trakingNumber = models.CharField(max_length=500,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date_time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"{self.name}"







class Feedback(models.Model):
  
    user = models.ForeignKey(UserAccount, related_name='feedback', on_delete=models.CASCADE)
    rating = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    updated_at = models.CharField(max_length=1000, blank=True, null=True)
   
    def __str__(self):
        return f"Review by {self.UserAccount.email}"



class Return(models.Model):
   
    user = models.ForeignKey(UserAccount, related_name='Return', on_delete=models.CASCADE)
    orderID = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)
    application = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    isviewed = models.CharField(max_length=1000, blank=True, null=True, default="no")
   
    def __str__(self):
        return f"{self.UserAccount.email}"






class Coupon(models.Model):
    
    copon = models.CharField(max_length=1000, blank=True, null=True)
    porcentage = models.CharField(max_length=1000, blank=True, null=True)
    productId = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    expired_at = models.CharField(max_length=1000, blank=True, null=True)
   
    def __str__(self):
        return self.copon










class ScheduledEmail(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    welcome_sent = models.BooleanField(default=False)
    day1_sent = models.BooleanField(default=False)
    day2_sent = models.BooleanField(default=False)
    day3_sent = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.email






class test(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)  # assuming you have a title field
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True)
    listing_id = models.CharField(max_length=200, blank=True, null=True)
    agent = models.CharField(max_length=200, blank=True, null=True)
    is_read = models.BooleanField(default=False)



class home_page(models.Model):

    hero_1 = models.ImageField(blank=True, null=True)
    hero_2 = models.ImageField(blank=True, null=True)
    section_features = models.ImageField(blank=True, null=True)
    awards = models.CharField(max_length=200, blank=True, null=True)
    agents = models.CharField(max_length=200, blank=True, null=True)
    visites = models.CharField(max_length=200, blank=True, null=True)
    place_image_1 = models.ImageField(blank=True, null=True)
    place_title_1 = models.CharField(max_length=200, blank=True, null=True)
    place_image_2 = models.ImageField(blank=True, null=True)
    place_title_2 = models.CharField(max_length=200, blank=True, null=True)
    place_image_3 = models.ImageField(blank=True, null=True)
    place_title_3 = models.CharField(max_length=200, blank=True, null=True)
    place_image_4 = models.ImageField(blank=True, null=True)
    place_title_4 = models.CharField(max_length=200, blank=True, null=True)
    place_image_5 = models.ImageField(blank=True, null=True)
    place_title_5 = models.CharField(max_length=200, blank=True, null=True)
    place_image_6 = models.ImageField(blank=True, null=True)
    place_title_6 = models.CharField(max_length=200, blank=True, null=True)
    section_steps = models.ImageField(blank=True, null=True)

# for simple live chat 


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.content[:50]}'










# for live chat Rooms 


"""

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='created_rooms',
        null=True,
        blank=True
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='chat_rooms',
        blank=True
    )
    is_private = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.display_name or self.name

    @property
    def member_count(self):
        return self.members.count()

    @property
    def latest_message(self):
        return self.messages.last()

class Message(models.Model):
    MESSAGE_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('file', 'File'),
        ('system', 'System'),
    ]

    room = models.ForeignKey(
        ChatRoom, 
        on_delete=models.CASCADE, 
        related_name='messages'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='messages'
    )
    content = models.TextField()
    message_type = models.CharField(
        max_length=10, 
        choices=MESSAGE_TYPES, 
        default='text'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, blank=True)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    # For replies/threads
    parent_message = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='replies'
    )
    
    # Read receipts
    read_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='read_messages',
        blank=True
    )

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.user.email}: {self.content[:50]}..."

    @property
    def is_reply(self):
        return self.parent_message is not None

class OnlineUser(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name='online_users'
    )
    last_seen = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['user', 'room']

    def __str__(self):
        return f"{self.user.email} in {self.room.name}"

        """

import random
import string


class PhoneOTP(models.Model):
    phone_number = models.CharField(max_length=15, db_index=True)
    otp_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['phone_number', 'is_verified']),
        ]
    
    def save(self, *args, **kwargs):
        if not self.otp_code:
            self.otp_code = self.generate_otp()
        if not self.expires_at:
            from django.conf import settings
            expire_time = getattr(settings, 'PHONE_OTP_EXPIRE_TIME', 300)
            self.expires_at = timezone.now() + timezone.timedelta(seconds=expire_time)
        super().save(*args, **kwargs)
    
    def generate_otp(self):
        from django.conf import settings
        length = getattr(settings, 'PHONE_OTP_LENGTH', 6)
        return ''.join(random.choices(string.digits, k=length))
    
    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def is_max_attempts_reached(self):
        from django.conf import settings
        max_attempts = getattr(settings, 'PHONE_OTP_MAX_ATTEMPTS', 3)
        return self.attempts >= max_attempts
    
    def __str__(self):
        return f"OTP for {self.phone_number} - {self.otp_code}"