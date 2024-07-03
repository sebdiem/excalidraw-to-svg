# Stage 1: Build stage
FROM node:18-alpine AS build

WORKDIR /app

# Install system dependencies for building
RUN apk add --no-cache \
    build-base \
    cairo-dev \
    jpeg-dev \
    pango-dev \
    giflib-dev \
    librsvg-dev

# Install node dependencies
RUN npm install canvas excalidraw-to-svg

# Stage 2: Runtime stage
FROM node:18-alpine

WORKDIR /app

# Install runtime dependencies
RUN apk add --no-cache \
    cairo \
    jpeg \
    pango \
    giflib \
    librsvg

# Copy node modules
COPY --from=build /app/node_modules /app/node_modules
