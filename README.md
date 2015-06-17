### Requirements

* An activated python virtualenv.
* mongodb installed and running.

#### Considering you already have installed the dependencies, created and activated your virtualenv:


### Installing

Clone the repository and install it:

```bash 
git clone https://github.com/michaeltcoelho/iclinic.git
```

Go to `/iclinic` directory:

```bash
cd iclinic
```

Run the following command:

```bash
make install
```

# After installling

After installing the app, edit the `iclinic/apps/config.py` file with information about your mongodb running instance

```python

MONGO_HOST = 'your localhost'
MONGO_PORT = mongodb port
```

### Testing

Running tests:

```bash
make test
```

### Running

Running the application:

```bash
make run
```