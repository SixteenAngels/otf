FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json* ./
# Install dependencies including the 'serve' package for serving static files
RUN npm install --legacy-peer-deps && npm install -g serve

COPY . .

# Build the React app for production
RUN npm run build

EXPOSE 3000

# Serve the built application
CMD ["serve", "-s", "build", "-l", "3000"]
