# Day 3 – Apache HTTP Server on Windows (IIS Conflict & Service Setup)

## Objective
Install Apache HTTP Server on Windows manually and run it as a
persistent Windows service.

---

## What I Did Today

- Installed Apache HTTP Server manually (without XAMPP)
- Previously had IIS installed and running
- Faced port conflict due to IIS using port 80
- Reconfigured Apache to use port 8080
- Installed Apache as a Windows Service
- Debugged service startup failures
- Successfully ran Apache in background as a service

---

## Problems Faced

### 1. Port 80 Access Denied
- Apache failed to bind to port 80
- Error: `(OS 10013) Access forbidden`

**Cause:**
- IIS reserves port 80 using HTTP.sys

**Fix:**
- Changed Apache port to 8080 in `httpd.conf`

---

### 2. Apache Service Stopping Immediately
- Apache worked in foreground but not as a service
- Service state showed STOPPED

**Cause:**
- Missing / inaccessible logs directory

**Fix:**
- Created `C:\Apache24\logs`
- Ensured write permissions

---

### 3. Confusion Between Foreground and Service Mode
- Apache cannot run in both modes simultaneously

**Learning:**
- Stop foreground process before starting service

---

## Commands Used

```bash
httpd.exe -t
httpd.exe -k install
httpd.exe -k start
sc query Apache2.4
