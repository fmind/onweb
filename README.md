# onweb

Check the status of some website.

## Installation

```python
pip install onweb
```

## Documentation

```python
onweb https://google.com https://www.google.com
301     https://google.com
200     https://www.google.com
```

__Handle redirect code (e.g. 301):__

```python
onweb --redirect https://google.com https://www.google.com
200     https://www.google.com
200     https://www.google.com
```
