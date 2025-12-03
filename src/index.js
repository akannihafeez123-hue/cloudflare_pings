import endpoints from "../endpoints.json";

export default {
  async scheduled(event, env, ctx) {
    for (const url of endpoints) {
      try {
        const resp = await fetch(url);
        console.log(`Pinged ${url}, status: ${resp.status}`);
      } catch (err) {
        console.error(`Failed to ping ${url}:`, err.message);
      }
    }
  }
};
