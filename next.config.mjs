export default {
  eslint: {
    ignoreDuringBuilds: true,
  },
  webpack: (config) => {
    config.experiments = {
      topLevelAwait: true,
      layers: true,
    };
    config.infrastructureLogging = {
      level: "error",
    };
    return config;
  },
};
