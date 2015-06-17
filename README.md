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

MONGO_HOST = 'your localhost address'
MONGO_PORT = your mongodb port
```

#### We're almost there...Before running tests, make sure if you're running the application

### Running

Running the application:

```bash
make run
```

### Testing

Running tests:

```bash
make test
```
