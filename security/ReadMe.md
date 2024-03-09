
## JWT Tokens and FastAPI: A Practical Guide

### 1. **What is JWT?**
- **JSON Web Tokens (JWT)** are compact, URL-safe tokens used for securely transmitting information between parties.
- A JWT consists of three parts: **header**, **payload**, and **signature**.
- The header and payload are Base64-encoded JSON objects, while the signature ensures data integrity.

### 2. **Setting Up FastAPI with JWT Authentication**
1. **Install Dependencies**:
    - Install the necessary packages:
        ```bash
        pip install "python-jose[cryptography]"
        pip install "passlib[bcrypt]"
        ```

2. **Password Hashing**:
    - Hash user passwords before storing them in the database.
    - Use **PassLib** with the recommended algorithm, **Bcrypt**.
    - Example code snippet:
        ```python
        from passlib.context import CryptContext

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        def hash_password(password: str) -> str:
            return pwd_context.hash(password)
        ```

3. **JWT Token Creation and Verification**:
    - Use **python-jose** to generate and verify JWT tokens.
    - Example code snippet:
        ```python
        from jose import JWTError, jwt

        SECRET_KEY = "your-secret-key"
        ALGORITHM = "HS256"

        def create_jwt_token(data: dict) -> str:
            return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        def verify_jwt_token(token: str) -> dict:
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                return payload
            except JWTError:
                return None
        ```

4. **User Authentication Flow**:
    - When a user logs in, create a JWT token with relevant user data (e.g., user ID, role).
    - Include an expiration time (e.g., 1 week) to handle session validity.
    - Verify the token on subsequent requests to ensure the user is authenticated.

5. **FastAPI Dependency Injection**:
    - Use FastAPI's dependency injection to handle authentication.
    - Example code snippet:
        ```python
        from fastapi import Depends, HTTPException
        from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

        oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

        def get_current_user(token: str = Depends(oauth2_scheme)):
            user = verify_jwt_token(token)
            if not user:
                raise HTTPException(status_code=401, detail="Invalid token")
            return user
        ```

6. **Protecting Routes**:
    - Use the `get_current_user` dependency to protect specific routes.
    - Example:
        ```python
        @app.get("/secure-data")
        def get_secure_data(current_user: dict = Depends(get_current_user)):
            # Your secure endpoint logic here
            return {"message": "Access granted!"}
        ```

### 3. **Testing and Deployment**
- Test your authentication flow thoroughly.
- Deploy your FastAPI application with JWT-based authentication to a production environment.

Remember that this guide provides a high-level overview. For detailed implementation, refer to the official FastAPI documentation and explore additional resources. Happy coding! 🚀
