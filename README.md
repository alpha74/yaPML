<img src="https://www.django-rest-framework.org/img/logo.png" height="100pm" width="250px">

## Django Rest Framework Demo

#### CRUD and Token login APIs


### Run

- Install packages from `requirements.txt`.
- Run command `python manage.py runserver`.

-----------

### APIs


#### User register

- `POST /localhost:8000/auth/register/`

- Sample input:

```
{
	"username": "jackd",
    	"email" : "jackt@yaPML.com",
	"password": "yaPML2023"
}
```

- Sample output:

```
201 CREATED
{
	"message" : "success"
}
```


-----------


#### User login

- `POST /localhost:8000/auth/login`

- Sample input:

```
{
	"username": "johnd",
	"password": "83rPAS*"
}
```

- Sample output:

```
{
	"token": "eyJhbGciOiJIUzI1NiIsInR"
}
```

-----------


#### Get products

- `GET /localhost:8000/products/` or
- `GET /localhost:8000/products/?page=2`

- Sample response

```
200 OK
{
    "count": 9,
    "next": "http://localhost:8000/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": "1",
            "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
            "price": "109.95",
            "category": "men's clothing",
            "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
            "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
        },
        {
            "id": "2",
            "title": "\"Mens Casual Premium Slim Fit T-Shirts",
            "price": "22.30",
            "category": "men's clothing",
            "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
            "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg"
        },
        {
            "id": "3",
            "title": "Mens Cotton Jacket",
            "price": "55.99",
            "category": "men's clothing",
            "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
            "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg"
        }
    ]
}
```

-----------

#### Add new product

- `POST /products/`

- Sample Input:

```
 {
    "id": "9",
    "title": "Grey Silver Plated Princess",
    "price": "500.99",
    "category": "jewelery",
    "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
    "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg"
}
```


- Sample Output:

```
201 CREATED
{
    "id": "10",
    "title": "Grey Gold Plated Princess",
    "price": "502.99",
    "category": "jewelery",
    "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
    "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg"
}
```
