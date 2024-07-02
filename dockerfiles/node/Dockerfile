# Step 1: Use an official Node runtime as a parent image
FROM node:22-slim

# Step 2: Set the working directory in the container
WORKDIR /usr/src/app

# Step 3: Copy the current directory contents into the container at /usr/src/app
COPY ./daybook-fe/. .

# Step 4: Install any needed packages specified in package.json
RUN npm install

# Step 5: Make port 3000 available to the world outside this container
EXPOSE 3000

# Step 6: Define environment variable
ENV REACT_APP_BACKEND_URL=http://localhost:8000

# Step 7: Run the app when the container launches
CMD ["npm", "start"]