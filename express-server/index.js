const axios = require("axios");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json())
app.post("/analyze-sentiment", (req, res)=>{
    let _text = req.body.text
    axios.post("http://127.0.0.1:5000/predict", {
        text: _text,
    }).then((vaderSentiment_res) => {
        res.send(vaderSentiment_res.data)
    });
});

app.listen(3000, () => {
  console.log("server starting at port 3000!");
});
