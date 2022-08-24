import express from "express";
import tf from "@tensorflow/tfjs";
import tmImage from "@teachablemachine/image";
import got from "got";
import { spawn } from "child_process";

const app = express();
const port = 3000;

app.post("/marksheet", async (req, res) => {
  const resultMarksheetComparison = await marksheetCompare(req, res);
  const resultMarskeetImageDataComparison = await marksheetImageDataComparison(
    req,
    res
  );
  const resultMarskeetApiDataComparison = await marksheetApiDataComparison(
    req,
    res
  );
  res.json({
    marksheet_comparison: resultMarksheetComparison,
    data_comparison_with_marksheet: resultMarskeetImageDataComparison,
    data_comparison_with_database: resultMarskeetApiDataComparison,
  });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

async function marksheetCompare(req, res) {
  return "matched"
  const URL = "E:project\nodepj\teachablemetadata.json";
  const modelURL = "E:project\nodepj\teachablemetadata.json";
  const metadataURL = "E:project\nodepj\teachablemodel.json";
  const model = await tmImage.load(modelURL, metadataURL);

  const path = "E://project//node//pj//image//SashiDo_Dog.jpg";
  const prediction = await model.predict(path);

  console.log(prediction);
}

async function marksheetImageDataComparison(req, res) {
  return "matched";
  var dataToSend;
  const python = spawn("python", ["script.py"]);

  python.stdout.on("data", async function (data) {
    dataToSend = data.toString().trim();

    console.log(dataToSend);
    return dataToSend;
  });

  python.stderr.on("data", (data) => {
    console.log(`Error${data}`);
  });
  // in close event we are sure that stream from child process is closed
  python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
  });

  console.log(dataToSend);
  return dataToSend;
}

async function marksheetApiDataComparison(req, res) {
  return "matched";
  const url =
    "https://script.google.com/macros/s/AKfycbyXyMMrgbw2HpSFk0GkmMvDFshW50I3Re9T8yBZKNtTeYjvvrQrCcmsbUtZbN2cafK1cg/exec";

  const data = await got.post(url, {
    json: {
      name: "Ronak Gupta",
      rollno: "158730",
    },
  });

  return data;
}
