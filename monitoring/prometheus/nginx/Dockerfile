FROM nginx:1.23-alpine
COPY nginx/active_active.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]