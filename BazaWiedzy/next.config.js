/** @type {import('next').NextConfig} */
const nextConfig = {
  basePath: "/bw",
  webpack: (config, { dev }) => {
    if (!dev) return config;
    // Solve compiling problem via vagrant
    config.watchOptions = {
      poll: 1000, // Check for changes every second
      aggregateTimeout: 300, // delay before rebuilding
    };
    return config;
  },
};

module.exports = nextConfig;
