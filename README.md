# HimeServ
HimeServ is a "Home File Access Server". Using Nginx and Filebrowser to access files stored on my old laptop (arch) via a web browser in a local network.

## Instructions

1. Install Nginx and Filebrowser:

```sh
sudo pacman -S nginx
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash
```

2. Edit Nginx configuration file for http:

```sh
sudo nvim /etc/nginx/nginx.conf
```
- Use this file [nginx.conf](nginx.conf) to direct the http request to the filebrowser service. 

3. Start & Enable Nginx:

```sh
sudo systemctl start nginx
sudo systemctl enable nginx
```

4. Start FileBrowser:

```sh
sudo filebrowser -r <location_of_directory_to_serve> -a <ip_of_your_old_laptop> -p 8080
```
- Access the FileBrowser by navigating to ``http://<ip_of_your_old_laptop>:8080`` in a web browser.

- Default credientials:
    - Username: `admin`
    - Password: `admin`

### Systemd Service Setup
5. Create configuration file:

```sh
sudo nvim /etc/filebrowser/filebrowser.json
```
- Use this file [filebrowser.json](filebrowser.json) to hold command-line arguments for server to run automatically.

- Remove the default created filebrowser.db from <location_of_directory_to_serve>.
```sh
sudo rm /<location_of_directory_to_serve>/filebrowser.db
```

- Run FileBrowser:

```sh 
sudo filebrowser -c /etc/filebrowser/filebrowser.json
```

6. Change Permissions for `.json` & `.db` file:

```sh
sudo chown <User>:<Group> /etc/filebrowser/filebrowser.*
```

- Note: Set `User` & `Group` same as in [filebrowser.service](filebrowser.service).

- Check using:
```sh
ls -la /etc/filebrowser/filebrowser.*
```

7. Add System service:

```sh
sudo nvim /etc/systemd/system/filebrowser.service
```

- Use this file [filebrowser.service](filebrowser.service) to setup service.

8. Run the FileBrowser Service:

```sh
cd /etc/systemd/system/
sudo systemctl enable filebrowser.service
sudo systemctl start filebrowser.service
sudo systemctl status filebrowser.service
sudo systemctl restart nginx
```

## #Note: 
Make the IP address of the server laptop static from the local network router.
