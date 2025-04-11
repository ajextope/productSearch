Django Image Search E-Commerce Deployment Guide
=============================================

1. PREREQUISITES
----------------
- Docker 20.10+
- Docker Compose 1.29+
- 4GB RAM (minimum)
- 10GB disk space

2. QUICK DEPLOYMENT
-------------------
1. Clone repository:
   git clone https://github.com/your-repo/ecommerce-image-search.git
   cd ecommerce-image-search

2. Configure environment:
   cp .env.example .env
   nano .env  # Edit with your settings

3. Build and launch:
   docker-compose up -d --build

4. Initialize database:
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser

5. Access application:
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

3. PRODUCTION SETUP
-------------------
For production, add to docker-compose.yml:

nginx:
  image: nginx:alpine
  ports:
    - "80:80"
    - "443:443"
  volumes:
    - ./nginx.conf:/etc/nginx/conf.d/default.conf
    - ./ssl:/etc/nginx/ssl
  depends_on:
    - web

4. MAINTENANCE COMMANDS
-----------------------
- View logs: docker-compose logs -f
- Restart: docker-compose restart web
- Backup DB: docker-compose exec web bash -c "cp db/db.sqlite3 db/backup-$(date +%Y-%m-%d).sqlite3"
- Enter shell: docker-compose exec web bash

5. TROUBLESHOOTING
------------------
- Port conflicts: Check ports 8000/80 availability
- Memory issues: Increase Docker resources
- Image processing: Verify OpenCV in container

6. OPTIONAL MONITORING
---------------------
Add to docker-compose.yml:

monitoring:
  image: prom/prometheus
  ports:
    - "9090:9090"
  volumes:
    - ./prometheus.yml:/etc/prometheus/prometheus.yml

Note: For production, consider PostgreSQL and Redis for better performance.