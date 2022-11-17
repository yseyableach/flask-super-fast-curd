## Migration

### install package

```
pip install flask-migrate
```

### Create Migration

1. flask db migrate -"migration_name"
2. Find the file with timestamp and write migrations into `up`, `down` function

### Generate Migration

1. flask db migrate

### Run Migration

1. flask db upgrade

### Revert Migration

1. flask db downgrade