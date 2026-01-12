# Automated SemVer Backend

Django REST API with automated semantic versioning for testing purposes.

## Features

- Widget and Cog REST API endpoints
- Version endpoint at `/api/version/`
- Automated semantic versioning using python-semantic-release
- Docker containerization

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start the development server:
```bash
python manage.py runserver
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET /api/widgets/` - List all widgets
- `POST /api/widgets/` - Create a widget
- `GET /api/widgets/{id}/` - Get a specific widget
- `PUT /api/widgets/{id}/` - Update a widget
- `DELETE /api/widgets/{id}/` - Delete a widget
- `GET /api/cogs/` - List all cogs
- `POST /api/cogs/` - Create a cog
- `GET /api/cogs/{id}/` - Get a specific cog
- `PUT /api/cogs/{id}/` - Update a cog
- `DELETE /api/cogs/{id}/` - Delete a cog
- `GET /api/version/` - Get API version

## Semantic Versioning

This project uses [python-semantic-release](https://python-semantic-release.readthedocs.io/) for automated versioning.

Commit message format:
- `feat:` - New feature (minor version bump)
- `fix:` - Bug fix (patch version bump)
- `BREAKING CHANGE:` - Breaking change (major version bump)

