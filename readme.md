## build

```
docker build . -t pythonflask
```

## use

```
docker run -itd --rm --name node -p 8080:80 pythonflask
```