#!/usr/bin/env pytest

import pytest

import onweb


@pytest.mark.asyncio
async def test_check_200(session):
    url = "https://www.google.com/"
    res = await onweb.check(session, url)

    assert res.status == 200
    assert res.url.human_repr() == url


@pytest.mark.asyncio
async def test_check_301_with_redirect(session):
    url = "https://google.com/"
    res = await onweb.check(session, url, redirect=True)

    assert res.status == 200
    assert res.url.human_repr() == "https://www.google.com/"


@pytest.mark.asyncio
async def test_check_301_without_redirect(session):
    url = "https://google.com/"
    res = await onweb.check(session, url, redirect=False)

    assert res.status == 301
    assert res.url.human_repr() == url


def test_checkall(loop):
    url = [
        "https://google.com",
        "https://www.google.com",
        "https://www.google.com/nope",
    ]

    res = loop.run_until_complete(onweb.checkall(url))

    assert [r.status for r in res] == [301, 200, 404]
