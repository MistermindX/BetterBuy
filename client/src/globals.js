export const BASE_URL =
  process.env.NODE_ENV === 'production'
    ? process.env.VUE_APP_API_URL
    : 'http://localhost:5000'
