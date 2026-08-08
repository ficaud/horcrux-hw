# Horcrux Hardware
<div align="center">
<img src="doc/img/horcrux-logo.png" width="150" alt="Horcrux Core logo">

<br/>
<br/>
<br/>

[![Horcrux-core](https://img.shields.io/badge/Horcrux_core-v2.2.3-orange)](https://github.com/ficaud/horcrux-core)

</div>

This repository is a step-by-step guide that teaches **complete beginners** how to build a Horcrux device entirely from scratch.

This is about the hardware and how you can build it yourself. For more information about the software that run the device, go to [horcrux-core](https://github.com/ficaud/horcrux-core).

## What you will learn

- **The philosophy** behind Horcrux — why it exists and what problem it solves.
- **How to build** a Horcrux device — from the electronic components to the final assembly.
- **How to use it** — storing and recovering your secrets in practice.

## What is a Horcrux?

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

The core idea is to make this powerful technology available to everyone, giving you full ownership and control over your most sensitive information. All that, without relying on any third party or cloud service that could have a leak or close overnight.

## What secrets should I store in a Horcrux?

You can store pretty much anything you want to keep secret. However, I'd recommend being selective about what you put inside. A Horcrux is best reserved for your most important secrets — the ones you truly couldn't afford to lose.

Good candidates include, the master password that unlocks your password manager, the recovery phrase or keys that protect your cryptocurrency, or even a private keepsake you don't want to lose.

## How to build a Horcrux

Building your own Horcrux is a step-by-step journey. The steps below will walk you through each part of the process, from the hardware to how you handle your shares once they exist.

- [Learn more](doc/MICROCONTROLLER.md) about the brain of the Horcrux device.
- [Learn more](doc/CREATE_SHARES.md) about the best ways to create your shares.
- [Learn more](doc/DISTRIBUTE_SHARES.md) about the best ways to distribute your shares.
