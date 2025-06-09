# 🚀 Spring Boot with MongoDB

This project is part of my Java development portfolio, demonstrating the implementation of a RESTful API using Spring Boot integrated with MongoDB. The project was developed during Prof. Nélio Alves' course, focusing on enhancing my backend development skills.

## 🛠️ Technologies Used

- **Java 17**
- **Spring Boot 3.3.11**
- **Spring Data MongoDB**
- **MongoDB**
- **Maven**

## 📂 Project Structure

```
src
├── main
│   ├── java
│   │   └── com
│   │       └── cursojava
│   │           └── mongodb
│   │               ├── config
│   │               ├── domain
│   │               ├── dto
│   │               ├── repository
│   │               ├── resources
│   │               │   └── exception
│   │               ├── services
│   │               │   └── exception
│   │               └── util
│   └── resources
└── test
    └── java
```

## ✨ Features

- Complete CRUD operations for users
- Post creation and retrieval
- Text search in post titles and content
- Date range filtering for posts
- Exception handling with custom error responses
- Data Transfer Objects (DTOs) for API responses


## 🔍 API Endpoints

### Users
- `GET /users` - List all users
- `GET /users/{id}` - Find user by ID
- `POST /users` - Create new user
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user
- `GET /users/{id}/posts` - List posts by user

### Posts
- `GET /posts/{id}` - Find post by ID
- `GET /posts/titlesearch?text={text}` - Search posts by title
- `GET /posts/fullsearch?text={text}&minDate={date}&maxDate={date}` - Full search with filters

## ⚙️ How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/fabiomvalente/Demos/tree/main/spring-boot-mongodb.git
   ```

2. Navigate to the project directory
   ```bash
   cd spring-boot-mongodb
   ```

3. Make sure MongoDB is running on port 27017

4. Run the application using Maven:
   ```bash
   ./mvnw spring-boot:run
   ```

5. The API will be available at `http://localhost:8080`


## ✅ Features

- Implement RESTful APIs with Spring Boot
- Work with NoSQL databases (MongoDB)
- Apply development best practices
- Structure projects following architectural patterns

## 📫 API Testing

All endpoints can be tested using **Insomnia** or **Postman**. You can create a collection for testing CRUD operations on your entities.