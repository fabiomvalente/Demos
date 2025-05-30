# Spring Boot Webservice with JPA & Hibernate

This project was developed as part of a training exercise to explore key backend technologies using Java and Spring Boot. It demonstrates how to build RESTful web services with JPA/Hibernate and manage them through common development tools.

## 🚀 Technologies Used

- **Spring Boot**
- **JPA / Hibernate**
- **Apache Tomcat** (embedded)
- **Maven**
- **H2 Database** (for tests)
- **PostgreSQL** (for development)
- **Insomnia** (API testing)

## 📂 Project Structure

The project follows the standard Spring Boot structure:

```
src/
 └── main/
     ├── java/
     │   └── com/example/project/
     │       ├── controller/
     │       ├── model/
     │       ├── repository/
     │       └── service/
     └── resources/
         ├── application.properties
         ├── data.sql
         └── schema.sql
```

## ⚙️ How to Run

### Prerequisites

- Java 17 or higher
- Maven
- PostgreSQL running locally
- Optional: Insomnia or Postman

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/webservice-spring-hibernate.git
   cd webservice-spring-hibernate
   ```

2. Configure PostgreSQL in `src/main/resources/application.properties`:
   ```properties
   spring.datasource.url=jdbc:postgresql://localhost:5432/your_database
   spring.datasource.username=your_username
   spring.datasource.password=your_password
   ```

3. Build and run the application:
   ```bash
   mvn spring-boot:run
   ```

4. Access your endpoints:
   - Base URL: `http://localhost:8080/`

## 📫 API Testing

All endpoints can be tested using **Insomnia** or **Postman**. You can create a collection for testing CRUD operations on your entities.

## ✅ Features

- RESTful CRUD operations
- H2 database for lightweight testing
- JPA repositories for data access
- Separation of concerns with Service and Repository layers

## 📝 Notes

This is a demo/training project and not intended for production use. Error handling, validation, and security features may be minimal.

---

Made with ☕ and Spring Boot 🚀