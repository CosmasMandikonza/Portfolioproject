# Personal Portfolio — Self-Hosted Flask App on Bare-Metal Linux

A Flask web application I designed, containerized, and operate as a real production service on a **self-hosted CentOS Linux server I configured from the ground up**. Built during the MLH Fellowship (Production Engineering track), the interesting part of this project is less the site itself and more how it is deployed, supervised, and kept running: real infrastructure, not a sandbox.

 **Stack:** Python / Flask · Docker · Nginx · systemd · GitHub Actions

---

## Infrastructure & Operations (the interesting part)

This app runs as a self-hosted production service. The engineering focus was reliability and repeatable deployment on hardware I manage directly.

- **Self-hosted on bare-metal Linux.** Runs on a CentOS server I set up from scratch: OS configuration, users and permissions, networking, and the runtime, all managed from the Linux command line. No managed cloud platform.
- **systemd service management.** The application runs under systemd so it starts on boot, restarts automatically on failure, and is supervised like any first-class system service, with logs available through `journalctl`.
- **Containerized with Docker.** Packaged with a `Dockerfile` and orchestrated by separate `docker-compose.yml` (local) and `docker-compose.prod.yml` (production) definitions, so the environment is identical and reproducible everywhere.
- **Nginx reverse proxy + HTTPS.** Fronted by Nginx (config in `user_conf.d/`) for TLS termination and routing to the app.
- **CI/CD pipeline (GitHub Actions).** On every push, the workflow runs the test suite, then deploys the updated site and sends a notification, turning deploys into a safe, one-step, auditable process instead of manual SSH-and-pray.
- **One-command redeploy.** `redeploy-site.sh` rebuilds and rolls out the latest version cleanly.
- **Tested.** Endpoint and application tests run with `pytest` as part of the pipeline, so broken code does not ship.
- **Resilient by default.** Custom 404 and 500 error handling and input-validated forms keep the service graceful under bad input and failures.

**Deployment flow:**
```
git push  ->  GitHub Actions  (pytest -> build -> deploy -> notify)
                                     |
                                     v
     CentOS server (bare-metal) -- systemd --> Docker (compose) --> Flask app
                                     ^
                               Nginx (HTTPS, reverse proxy)
```

---

## Tech Stack

- **Application:** Python, Flask, Jinja2
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Infrastructure & Ops:** CentOS Linux, systemd, Docker and docker-compose, Nginx, GitHub Actions CI/CD, Bash
- **Testing:** pytest

---

## Run It Locally

```bash
git clone https://github.com/CosmasMandikonza/Portfolioproject.git
cd Portfolioproject
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp example.env .env        # then edit the values
flask run                  # http://127.0.0.1:5000
```

Or run it the way it runs in production, containerized:
```bash
docker compose up --build
```

---

## What This Project Demonstrates

- Standing up and operating a service on self-managed Linux hardware
- Process supervision and reliability with systemd
- Reproducible, containerized deployments
- Automated, tested CI/CD instead of manual deploys
- Practical debugging and day-to-day operations of a live web service

---

## The Site Itself

A responsive personal portfolio with a homepage, experience timeline, an interactive travel map, a hobbies page, and a validated contact form, built with Flask and Jinja2 templates and styled with Bootstrap and custom CSS.

---

**Author:** Cosmas Mandikonza · [github.com/CosmasMandikonza](https://github.com/CosmasMandikonza) · [linkedin.com/in/cosmas-mandikonza](https://www.linkedin.com/in/cosmas-mandikonza) · cosmas.t.mandikonza@gmail.com

_Built during the MLH Fellowship, Production Engineering track._
