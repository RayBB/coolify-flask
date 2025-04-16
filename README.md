# coolify-flask

I wanted to understand how I can deploy a flask app to coolify simply, without making my own dockerfile.

Coolify uses [Nixpacks](https://nixpacks.com/docs/getting-started) so that was the main thing to know.

Here's what you need to know:

First, create a `nixpacks.toml` to specify the start command.

Second, you'll probably want to use gunicorn or similar. Something like `gunicorn -w 4 -b 0.0.0.0:3000 main:app`.

Third, turn on GitHub webhooks and healthchecks in the coolify UI.

To run this locally:
`uv run gunicorn -w 4 -b 0.0.0.0:3000 main:app`

Overall, pretty simple once you understand all the parts.
