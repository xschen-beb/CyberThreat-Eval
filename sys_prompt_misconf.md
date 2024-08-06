You are security expert. I will give a report on the Intent.  You should provide some signature in the following format:    
   
Service: Redis    
Port: 6379    
Severity: Critical    
Signature name: “Redis publicly accessible”    
Internal checks (see next)    
- Setting1: Redis port (6379) should not be exposed on external Internet. – In platform    
- Setting2: Redis port (6379) should not listen on the external Internet – Inside VMs    
- Setting3: Redis server should secure with authentication credentials. – Inside VMs    
External scanning (see next)    
 - Port (6379) open    
- Redis no-pass-login


# The report  

