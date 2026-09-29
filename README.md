# TikTok Profile Scraper - Followers, Likes & Latest Videos

**Run it on Apify: [apify.com/clearfetch/tiktok-profile-scraper](https://apify.com/clearfetch/tiktok-profile-scraper)**

Scrape TikTok profiles without logging in. For every username you get the account's followers, following, total
likes, video count, bio, bio link and verified flag, plus its latest videos with views, likes, shares, comments,
saves, post time and duration. **$1.00 per 1,000 results.** No cookies, no proxy, no browser.

## What data you get

**One profile row per account:** `followers`, `following`, `likes`, `videoCount`, `friendCount`, `bio`, `bioLink`,
`verified`, `privateAccount`, `nickname`, `userId`, `secUid`, account creation date (`createTimeISO`), `language`,
`avatarUrl`, and `videosListed`, how many of its videos follow in the dataset.

**One row per video** (the account's latest, up to 10):

- `playCount`, `diggCount` (likes), `shareCount`, `commentCount`, `collectCount` (saves), `repostCount`
- `createTimeISO`, `durationSeconds`, `text` (caption), `hashtags`, `mentions`, `textLanguage`, `locationCreated`,
  `isAd`, `isAiGenerated`
- Sound: `musicTitle`, `musicAuthor`, `musicOriginal`, `musicUrl`; author stats repeated on every row

## How to use

1. Add usernames (with or without @) or profile links, one per line.
2. Optionally keep only recent videos (**Only videos newer than**: "7 days", "2026-09-01") or cap videos per account.
3. Run it, then download JSON, CSV or Excel, or pull the rows through the API. Schedule it daily to track growth.

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `profiles` | array | — | Usernames or profile links. Also `usernames`, `startUrls`. |
| `fetchVideoDetails` | boolean | `true` | Read each video's page for likes, shares, comments, saves, sound and author stats. Off is faster and keeps views, caption, cover and date. |
| `newerThan` | string | — | A date or an age like `"7 days"`. Older videos are left out and not charged. |
| `maxVideosPerSource` | integer | `0` | Videos per account. `0` means all TikTok lists (up to 10). |
| `includeSummaryRows` | boolean | `true` | The profile row itself. Turn off to get videos only. |
| `includeRaw` | boolean | `false` | Add TikTok's untouched objects as `raw`. |
| `maxConcurrency` | integer | `3` | Pages read in parallel. |
| `timeoutSecs` | integer | `30` | Per request. |
| `proxyConfiguration` | object | off | Not needed. |

## Output example

A real profile row from a run with `"profiles": ["nasa"]` (avatar link shortened):

```json
{
  "ok": true,
  "type": "profile",
  "username": "nasa",
  "nickname": "NASA",
  "userId": "7664638705177150477",
  "secUid": "MS4wLjABAAAAU9BRVzC8oCaegVnia8IbqWhPb_-dbU7s00Y3wS1_Nx8g5RUaYvyXrpejgjdxTwd6",
  "url": "https://www.tiktok.com/@nasa",
  "bio": "Making the seemingly impossible, possible.✨",
  "bioLink": null,
  "verified": true,
  "privateAccount": false,
  "followers": 1867774,
  "following": 23,
  "likes": 9780475,
  "videoCount": 49,
  "friendCount": 17,
  "createTimeISO": "2026-07-20T15:55:49.000Z",
  "language": "en",
  "avatarUrl": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068...",
  "videosListed": 5,
  "note": null,
  "inputUrl": "nasa",
  "scrapedAt": "2026-09-29T13:51:37.465Z"
}
```

Video rows have the same columns as in the example of the [TikTok Video Scraper](https://apify.com/clearfetch/tiktok-video-scraper).
An account that does not exist or cannot be read comes back as one row with `ok: false` and a plain reason, free.

## Pricing

**$1.00 per 1,000 results**: one charge per profile or video row written. Accounts that fail and videos filtered
out by `newerThan` are free.

## Use cases

- **Influencer vetting**: followers, likes per video and posting frequency before you reach out.
- **Competitor and creator tracking**: a daily schedule on a list of accounts shows follower growth and how each
  new video performs.
- **Lead lists**: bio links and verified flags for a list of creators in a niche.

## FAQ

**How many videos per profile?** The latest 10, which is what TikTok's embed player lists. TikTok's full
profile feed needs signed, logged-in requests, which this Actor does not forge. For older videos, use video links
with the [TikTok Video Scraper](https://apify.com/clearfetch/tiktok-video-scraper).

**Do I need a proxy or cookies?** No. Everything comes from public TikTok pages that load without an account.
The proxy option exists for very large scheduled volumes only.

**Is it legal?** It reads only public pages, the same ones anyone sees without logging in. You are responsible
for how you use the data, including data protection rules for personal data such as usernames.

## Integrations

Run it from the Apify API or a client library, schedule it in Apify Console, or connect it to n8n, Make,
Zapier or any MCP client through Apify's integrations. Results are available as JSON, CSV, Excel and through
the dataset API.

## Changelog

- **1.0.0** (2026-09) — first release: profile stats and the latest videos per account, date filter.
