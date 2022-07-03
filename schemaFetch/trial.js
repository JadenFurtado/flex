const express = require('express');
const app = express();
'use strict';
const puppeteer = require('puppeteer');
const request_client = require('request-promise-native');

const getData = async () => {
  try {
      var netResult = [];
      var endpoint = "server.club.ndl.iitkgp.ac.in";
      (async () => {
      const browser = await puppeteer.launch();
      const page = await browser.newPage();
      const result = [];

      await page.setRequestInterception(true);

      page.on('request', request => {
        request_client({
          uri: request.url(),
          resolveWithFullResponse: true,
        }).then(response => {
          const request_url = request.url();
          const request_headers = request.headers();
          const request_post_data = request.postData();
          const response_headers = response.headers;
          const response_size = response_headers['content-length'];
          const response_body = response.body;

          result.push({
            request_url,
            request_headers,
            request_post_data,
            response_headers,
            response_size,
            response_body,
          });
          netResult.push(result);
          console.log(result);
          request.continue();
        }).catch(error => {
          console.error(error);
          request.abort();
        });
      });

      await page.goto('https://'+endpoint, {
        waitUntil: 'networkidle0',
      });
      await browser.close();
      return netResult;
    })();
  } catch (err) {
     console.log(err)
  }
  
}

getData()