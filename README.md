# InboxOS

AI-powered Gmail workspace for intelligent email management and productivity.

## Tech Stack

### Frontend
- Next.js
- TypeScript
- TailwindCSS
- shadcn/ui

### Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic

### AI
- OpenAI (planned)

## Current Progress

### Completed
- Project structure
- FastAPI backend setup
- Next.js frontend setup
- PostgreSQL database setup
- SQLAlchemy models
- Alembic migrations
- Google OAuth login
- Session management
- User authentication endpoint (`/auth/me`)

### In Progress
- Persist authenticated users to PostgreSQL

### Planned
- Gmail account connection
- Gmail inbox sync
- Email threads and messages
- AI summaries
- Task extraction
- Priority classification
- Dashboard views

## Local Development

### Backend

```bash
cd apps/api
source venv/bin/activate
uvicorn app.main:app --reload
```

### Frontend

```bash
cd apps/web
npm run dev
```
