# FedEx Operations Metrics


## GitHub
- For access, email: jra457@msstate.edu
 
- Link: https://github.com/jra457/CHI


## Software/Templates
- Back-End:
  - Python based Django Application
  - Data stored in SQL Database
 
- Front-End:
  - Implemented with Bootstrap
  - Located in operations/opMetrics/static/
   - Main Files:
     - bootstrap.css
     - bootstrap.js
  
- Development:
  - All development was done in VS Code


## File Layout
- operations/  
  - manage.py  
  - fedex/  
    - __pychace__  
    -	asgi.py  
    - __init__.py  
    -	settings.py  
    -	urls.py  
    - wsgi.py  
  - opMetrics/  
    - admin.py  
    - apps.py  
    - forms.py  
    - models.py  
    - tests.py  
    - urls.py  
    - __init__.py  
    - views.py  
    - migrations/  


## Details[^note]

- operations/ # Website folder  

   - manage.py          # Script to run Django tools for this project (created using django-admin)  

   - operations/        # Website/project folder (created using django-admin)  

   - opMetrics/ 	  # Application folder (created using manage.py)  

     - __init__.py # Empty file that instructs Python to treat this directory as a Python package.  

     - settings.py # Contains all the website settings, including registering any applications we create,
                     the location of our static files, database configuration details, etc.  

     - urls.py     # Defines the site URL-to-view mappings. While this could contain all the URL mapping code,
                     it is more common to delegate some of the mappings to particular applications, as you'll see later.  

     - wsgi.py     # Used to help your Django application communicate with the webserver. You can treat this as boilerplate.  

     - asgi.py     # Standard for Python asynchronous web apps and servers to communicate with each other.  
                     ASGI is the asynchronous successor to WSGI and provides a standard for both asynchronous and synchronous
                     Python apps (whereas WSGI provided a standard for synchronous apps only). It is backward-compatible with 
                     WSGI and supports multiple servers and application frameworks.  
                   
                   
## Implemented Apps
- operationsMetrics (home)  
- packagesPerHour  
- DEX  
- volumeAvailabilityStatus  


## Company Layout
Division  
&ensp;Region  
&ensp;&ensp;District  
&ensp;&ensp;&ensp;location  
&ensp;&ensp;&ensp;&ensp;Senior Manager  
&ensp;&ensp;&ensp;&ensp;Type  
&ensp;&ensp;&ensp;&ensp;State  


[^note]:
    Detail information from MDN Web Docs (Mozilla Developer Network).    
    Link: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
