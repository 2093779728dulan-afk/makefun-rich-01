# 注意：计划文本必须用英文写。
import os

PLAN = """1. Hold $2 (2%) for refunds; deploy $98. No crypto trading, betting, stocks, arbitrage, or ID/phone checks.
2. Day 1: create email + seller accounts on API-based micro-gig marketplaces and crypto-bounty boards; agent signup, posting, bidding, messaging, payouts; no KYC.
3. Publish samples: 200-word ad copy, clean 100-row CSV, 5 bug fixes with tests.
4. List 5 $5 gigs: copy, CSV cleanup, bug fixes, README, tests; script intake, 1h delivery.
5. Days 1-3: API-apply to 20-30 posts/day; win ~1/day at $5; refunds from reserve.
6. Days 4-7: $5-8, 1 job/day, ask ratings, reinvest in bids; $40 by day 7.
7. Week 2: 5+ ratings, $12-15, ~6 jobs; $120 by day 14.
8. Week 3: $20-30, ~7 jobs, scripted QA; ~$280 by day 21.
9. Week 4: $40-60, 1-2 jobs/day (12-13 total); ~$900 by day 30.
10. Daily: log posts, wins, prices, ratings, refunds; drop flagged boards."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PLAN)


if __name__ == "__main__":
    main()
