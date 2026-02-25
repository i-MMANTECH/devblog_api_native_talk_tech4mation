Here is a single, clean, consolidated `README.md` file that compiles **everything we worked on today** into one professional document.  
No fluff, no repetition — just the essential structure, setup, features, endpoints, and notes from the full session.

Copy-paste this directly into your project root as `README.md`:

```markdown
# DevBlog API

A complete RESTful blog backend built with **Django** and **Django REST Framework (DRF)**.  
Developed as a hands-on learning project on February 25, 2026 — covers JWT authentication, ownership permissions, post-comment relationships, filtering/search/pagination, and full CRUD testing in Postman.

## Features

- JWT authentication (access + refresh tokens)
- Posts: create, list, retrieve (by slug), update, delete
- Comments: nested under posts — create, list, update, delete
- Tags: ManyToMany relationship (created on-the-fly or reused)
- Permissions: read public, write authenticated, edit/delete only by owner
- Filtering: by tag name, author username
- Search: in title and content
- Ordering: by created_at, title
- Pagination: 10 items per page
- Automatic slug generation from title
- Timestamps: created_at, updated_at

## Tech Stack

- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt (JWT auth)
- django-filter (filtering)
- Python 3.10+

## Project Structure

```
devblog_api/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── blog/
│   ├── migrations/
│   ├── models.py          # Post, Comment, Tag
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
├── venv/
└── README.md
```

## Setup

1. Activate virtual environment

   ```bash
   # Windows
   venv\Scripts\activate
   ```

2. Install dependencies

   ```bash
   pip install django djangorestframework djangorestframework-simplejwt django-filter
   ```

3. Apply migrations & create superuser

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run server

   ```bash
   python manage.py runserver
   ```

   Base URL: `http://127.0.0.1:8000/api/`

## API Endpoints

| Method | Endpoint                                      | Description                              | Auth     |
|--------|-----------------------------------------------|------------------------------------------|----------|
| POST   | `/api/auth/token/`                            | Obtain JWT access & refresh tokens       | Yes      |
| POST   | `/api/auth/token/refresh/`                    | Refresh access token                     | Yes      |
| GET    | `/api/posts/`                                 | List posts (paginated, searchable)       | Public   |
| POST   | `/api/posts/`                                 | Create new post                          | Auth     |
| GET    | `/api/posts/<slug>/`                          | Retrieve single post                     | Public   |
| PATCH  | `/api/posts/<slug>/`                          | Partial update own post                  | Owner    |
| DELETE | `/api/posts/<slug>/`                          | Delete own post                          | Owner    |
| GET    | `/api/posts/<slug>/comments/`                 | List comments on post                    | Public   |
| POST   | `/api/posts/<slug>/comments/`                 | Create comment on post                   | Auth     |
| GET    | `/api/comments/<id>/`                         | Retrieve comment                         | Public   |
| PATCH  | `/api/comments/<id>/`                         | Update own comment                       | Owner    |
| DELETE | `/api/comments/<id>/`                         | Delete own comment                       | Owner    |

### Query Parameters (for `/api/posts/`)

- `?search=keyword` → search title/content
- `?tags__name=django` → filter by tag
- `?author__username=admin` → filter by author
- `?ordering=-created_at` → sort newest first

## Authentication Flow (Postman)

1. **Login** → POST `/api/auth/token/`

   ```json
   {
       "username": "your_username",
       "password": "your_password"
   }
   ```

   → Save `access` token as `access_token` variable

2. Use `Authorization: Bearer {{access_token}}` for protected requests

3. Refresh when expired → POST `/api/auth/token/refresh/`

   ```json
   {
       "refresh": "{{refresh_token}}"
   }
   ```

## Postman Testing Summary

- JWT login → tokens obtained
- Post creation with tags → 201 Created
- Comment creation → 201 Created (post auto-assigned after serializer fix)
- Post update (PATCH) → 200 OK
- Attempted edit by non-owner → 403 Forbidden
- Unauthenticated write → 401 Unauthorized
- Public read (GET) → 200 OK without token
- Slug-based lookup fixed → no more 404 on wrong placeholder

## Lessons Learned / Practiced

- JWT lifecycle (obtain, use, refresh)
- Custom permission class (`IsOwnerOrReadOnly`)
- Nested serializers & ManyToMany handling
- SlugField + auto-generation
- DRF filters: search, django-filter, ordering, pagination
- Common Postman/DRF debugging:
  - 400 missing required fields
  - 404 wrong slug / placeholder misuse
  - 401/403 authentication & ownership issues

## Next Possible Steps

- User registration endpoint
- Rich text / markdown support
- Likes, categories, or drafts
- OpenAPI/Swagger docs (drf-spectacular)
- Deployment (Render, Railway, etc.)

Emmanuel Aro (imman_tech)
Lagos, Nigeria  
February 25, 2026
```

This version is concise, scannable, and professional — perfect for GitHub, portfolio, or sharing with mentors.  
It captures the full journey without overwhelming detail.

If you want any section expanded, shortened, or a `requirements.txt` added, just tell me.

What would you like to do now?  
- Push to GitHub?  
- Add registration?  
- Deploy?  
- Start a new project?  
- Rest and celebrate? 😊