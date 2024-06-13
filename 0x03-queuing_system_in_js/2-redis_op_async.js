import { createClient } from "redis";
import { promisify } from "util";
const redis = require("redis");

const client = createClient().on("error", (err) =>
  console.log("Redis client not connected to the server:", err.message)
);
console.log("Redis client connected to the server");

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  get(schoolName).then((res) => {
    console.log(res);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
