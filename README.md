# Horcrux Hardware

This repository is a step-by-step guide that teaches **complete beginners** how to build a Horcrux device entirely from scratch.

## What you will learn

By following this guide, you will learn:

- **The philosophy** behind Horcrux — why it exists and what problem it solves.
- **How to build** a Horcrux device — from the electronic components to the final assembly.
- **How to use it** — storing and recovering your secrets in practice.

## Introduction

A **Horcrux** is a physical device that lets you safely store your most sensitive secrets.

Under the hood, it relies on the [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) algorithm that works the following way:

1. Your secret is **split into multiple pieces** (called *shares*).
2. Each share is useless on its own — you cannot recover the secret from a single share.
3. To reconstruct the secret, you need to bring together at least a **threshold number** of shares.

This means you can distribute your shares across different locations or people, and even if some shares are lost or stolen, your secret remains safe as long as the threshold isn't reached.

## Why Horcrux?

Horcrux aims to implement Shamir's Secret Sharing in a way that is:

- **Timeless** — built with durable, long-lasting hardware.
- **Private** — horcrux is not connected to the itnernet.
- **Secure** — designed to protect your data against theft and loss.
- **Open source** — anyone can build its own horcrux device for almost nothing.

The core idea is to make this powerful technology available to everyone, giving you full ownership and control over your most sensitive information — without relying on any third party or cloud service that could have a leak or close overnight.
