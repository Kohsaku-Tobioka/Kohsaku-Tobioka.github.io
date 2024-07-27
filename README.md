
# Kohsaku Tobioka's Homepage

![pages-build-deployment](https://github.com/academicpages/academicpages.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)

[https://kohsaku-tobioka.github.io/](https://kohsaku-tobioka.github.io/)

## [WIP] How to update the Homepage

- _pages
  - 基本的な構成として `.md` ファイルは HP に表示される内容を直接このファイルだけで記述するもので、`.html` ファイルは該当ディレクトリのファイルを複数個読み込んで表示するためのもの（つまり内容を更新したい場合は `.html` はいじらず該当ディレクトリの中身をいじる）
  - `about.md`: トップページの内容を記述する markdown ファイル
  - `cv.md`: CV ページの内容を記述する markdown ファイル
  - `forfun.md`: For fun ページの内容を記述する markdown ファイル
  - `japanese.md`: 日本語自己紹介の内容を記述する markdown ファイル
  - `teachmentor.md`: Mentoring&Teaching ページの内容を記述する markdown ファイル
  - `news.html`: News ページの記述をする html ファイルで、中身は _posts ディレクトリのファイル読み込み
  - `research.html`: Research ページの記述をする html ファイルで、中身は _research ディレクトリのファイル読み込み
  - `talkmap.html`: To Be Updated
  - `talks.html`: Talks ページの記述をする html ファイルで、中身は _talks ディレクトリのファイル読み込み
- _posts (_news に変えたかったが変更がちょっと大変なのでこのまま)
  - News の内容を記述する各ファイル 
- _research
  - Research の内容を記述する各ファイル
- _talks
  - Talks の内容を記述する各ファイル
- files
  - 論文とか講演資料の pdf ファイルを置く場所
- images
  - 画像ファイルを置く場所

## Running Locally

When you are initially working your website, it is very useful to be able to preview the changes locally before pushing them to GitHub. To work locally you will need to:

1. Clone the repository and made updates as detailed above.
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `jekyll serve -l -H localhost` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

If you are running on Linux it may be necessary to install some additional dependencies prior to being able to run locally: `sudo apt install build-essentials gcc make`

## Acknowledgement
This repository is based on [https://github.com/academicpages/academicpages.github.io](https://github.com/academicpages/academicpages.github.io).