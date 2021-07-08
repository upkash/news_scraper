import requests
import json
from database import session
from bs4 import BeautifulSoup
import nltk
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# # nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

url = "https://finance.yahoo.com/_finance_doubledown/api/resource?bkt=fdw-MASTonQSP-5%2Cxray-us-finance-desktop-minicard-4&crumb=dY6cN.CFKNe&device=desktop&ecma=modern&feature=adsMigration%2CcanvassOffnet%2CccOnMute%2CdisableCommentsMessage%2Cdebouncesearch100%2CdeferDarla%2CecmaModern%2CemptyServiceWorker%2Cenable3pConsent%2CenableCCPAFooter%2CenableCMP%2CenableConsentData%2CenableFeatureTours%2CenableFinancialsTemplate%2CenableFreeFinRichSearch%2CenableGuceJs%2CenableGuceJsOverlay%2CenableNavFeatureCue%2CenableNewResearchInsights%2CenablePfSummaryForEveryone%2CenablePremiumSingleCTA%2CenablePrivacyUpdate%2CenableRebranding%2CenableStreamDebounce%2CenableTheming%2CenableUpgradeLeafPage%2CenableVideoURL%2CenableXrayNcp%2CenableXrayNcpInModal%2CenableXrayTickerEntities%2CenableYahooSans%2CenableYodleeErrorMsgCriOS%2CncpListStream%2CncpPortfolioStream%2CncpQspStream%2CncpStream%2CncpStreamIntl%2CncpTopicStream%2CnewContentAttribution%2CnewLogo%2CoathPlayer%2CoptimizeSearch%2Cpremium35%2CrelatedVideoFeature%2CreportReactMarkupDiff%2CthreeAmigos%2CwaferHeader%2CuseNextGenHistory%2CvideoNativePlaylist%2CsunsetMotif2%2CenableUserPrefAPI%2Clivecoverage%2CdarlaFirstRenderingVisible%2CenableAdlite%2CenableTradeit%2CenableFeatureBar%2CenableSearchEnhancement%2CenableUserSentiment%2CenableBankrateWidget%2CenableYodlee%2CcanvassReplies%2CenablePremiumFinancials%2CenableInstapage%2CenableNewResearchFilterMW%2CshowExpiredIdeas%2CshowMorningStar%2CenableSEOResearchReport%2CenableSingleRail%2CenableUpgrade%2CenableAmexOffer%2CenableUserInsights%2CenhanceAddToWL%2Carticle2_csn%2CsponsoredAds%2CenableStageAds%2CenableTradeItLinkBrokerSecondaryPromo%2CenableQspPremiumPromoSmall%2CclientDelayNone%2CthreeAmigosMabEnabled%2CthreeAmigosAdsEnabledAndStreamIndex0%2CenableRelatedTickers%2CenableTasteMaker%2CenableNotification%2CenableJSErrorBeacon%2CfinanceRightRailA20%2CenableBrokerCenter%2CenableYahooPlus%2CenablePremiumUpsell&intl=us&lang=en-US&partner=none&prid=049ol61gckguh&region=US&site=finance&tz=America%2FLos_Angeles&ver=0.102.4901"
requested_count = 140
remaining_count = 140
payload = json.dumps({
    "requests": {
        "g0": {
            "resource": "StreamService",
            "operation": "read",
            "params": {
                "ui": {
                    "comments_offnet": True,
                    "editorial_featured_count": 1,
                    "image_quality_override": True,
                    "link_out_allowed": True,
                    "needtoknow_template": "filmstrip",
                    "ntk_bypassA3c": True,
                    "pubtime_maxage": 0,
                    "relative_links": True,
                    "show_comment_count": True,
                    "smart_crop": True,
                    "storyline_count": 2,
                    "storyline_enabled": True,
                    "storyline_min": 2,
                    "summary": True,
                    "thumbnail_size": 100,
                    "tiles": {
                        "allowPartialRows": True,
                        "doubleTallStart": 0,
                        "featured_label": False,
                        "gradient": False,
                        "height": 175,
                        "resizeImages": False,
                        "textOnly": [
                            {
                                "backgroundColor": "#fff",
                                "foregroundColor": "#000"
                            }
                        ],
                        "width_max": 300,
                        "width_min": 200
                    },
                    "view": "mega",
                    "editorial_content_count": 6,
                    "enable_lead_fallback_image": True,
                    "finance_upsell_threshold": 4
                },
                "category": "LISTID:db1d46e0-a969-11e9-bff5-6dfdb80d79cf",
                "forceJpg": True,
                "releasesParams": {
                    "limit": 20,
                    "offset": 0
                },
                "offnet": {
                    "include_lcp": True,
                    "use_preview": True,
                    "url_scheme": "domain"
                },
                "use_content_site": True,
                "useNCP": True,
                "video": {
                    "enable_video_enrichment": True
                },
                "ads": {
                    "ad_polices": True,
                    "contentType": "video/mp4,application/x-shockwave-flash,application/vnd.apple.mpegurl",
                    "count": 25,
                    "enableFlashSale": True,
                    "enableGeminiDealsWithoutBackground": True,
                    "frequency": 4,
                    "geminiPromotionsEnabled": True,
                    "generic_viewability": True,
                    "inline_video": True,
                    "partial_viewability": True,
                    "pu": "finance.yahoo.com",
                    "se": 4492794,
                    "spaceid": 1183308065,
                    "start_index": 1,
                    "timeout": 0,
                    "type": "STRM,STRM_CONTENT,STRM_VIDEO",
                    "useHqImg": True,
                    "useResizedImages": True
                },
                "batches": {
                    "pagination": True,
                    "size": 140,
                    "timeout": 1500,
                    "total": 170
                },
                "enableAuthorBio": True,
                "max_exclude": 0,
                "min_count": 3,
                "min_count_error": True,
                "service": {
                    "specRetry": {
                        "enabled": False
                    }
                },
                "pageContext": {
                    "pageType": "minihome",
                    "subscribed": "0",
                    "enablePremium": "1",
                    "eventName": "",
                    "topicName": "stock-market-news",
                    "category": "",
                    "quoteType": "",
                    "calendarType": "",
                    "screenerType": ""
                },
                "content_type": "topic",
                "content_site": "finance",
                "ncpParams": {
                    "body": {
                        "gqlVariables": {
                            "main": {
                                "pagination": {
                                    "requestedCount": requested_count,
                                    "remainingCount": remaining_count,
                                    "geminiToken": "{\"geminiDedupeToken\":\"ChM4NDI1OTMzMDExMjkzNjAyOTg3EpkDCjAIjb09EKHvmdiQ74PkTBjMvsWevfGK78IBIM7snoTVsqXKAyoLQmFueWFuIEhpbGwKNgiv2moQ9ryE96OP19ptGL_T7IWChtik6wEg6_qW27u_6KbeASoQQ29tY2FzdCBCdXNpbmVzcwo3CPSKaxC2gKKintC8lUUYhe-TyNmsrfQDIJzR0721wu_GrAEqEkZpc2hlciBJbnZlc3RtZW50cwo9CKz4chDYram5jdu9o0oY2ezWvfz685VcIMXYr9nG27udQyoZRW1waXJlIEZpbmFuY2lhbCBSZXNlYXJjaAo4CMDMcBCawt7kjonb2U0Yhs3M0cuFgPRUIMWu8J__gonh8gEqE0ludGVyYWN0aXZlIEJyb2tlcnMKLwiDrm4QmMy2gN--6tN0GP-_spbC4byfiQEgzMCPkZKK4PIHKgpTbWFydEFzc2V0Ci8Iso9pEPvFkbqNp4GgSRiRzY-RtPWhkE4gjYblqOjPx92fASoKQW1hem9uLmNvbRISNDA4NDA2Njk3Mjg0MDUxNTQzGAcg-puSAg\",\"adsStartIndex\":\"1\"}",
                                    "uuids": "5cc38ee1-4a52-3c1a-b2ed-ce299ff70020:STORY,9ebe03eb-1ec0-30a1-a166-bc3c61c0b3e7:STORY,da728d22-c254-3355-9a4b-a8f577103f7c:STORY,28e3b189-0f54-3cad-baea-124b061cc32d:STORY,af13edac-1532-33fc-9542-98bd0a7b1d1b:STORY,cbd0bca0-19a6-3e5a-9292-72df2c1b7a01:STORY,7b7cdd93-57b9-3244-b0cf-b07ee5cb251d:STORY,d46e8185-8b28-3d0c-9cc7-905a70352344:STORY,3eb15613-822d-3b95-ac9d-75f1e69bd284:STORY,4ab3a618-f640-3456-8bd3-d9488d4e0f41:STORY,9bb629ec-60e3-371e-9e2e-8419713d76c2:STORY,2c03c2c2-f6d2-3a5e-acac-3f1b4dc78c29:STORY,4a21cf9a-62b0-35f0-a61a-01460686e143:STORY,fead0ce3-4584-3d7c-b1c7-b2fe2ab916eb:STORY,b89a9517-1bcc-30a0-8b30-14f7f29da638:STORY,0c6c3035-afea-3d0e-87b4-2b3476f743f8:STORY,b1bb5fb6-2b8a-3a0d-888d-d1e693557485:STORY,97f95a6e-9fe3-3640-95cc-7a01cba481f2:STORY,7e64a578-c81e-37ea-86c5-848f550ce85f:STORY,2acf3cd8-f1a2-3a11-8765-6da241053921:STORY,9748acb7-48b3-31c1-a003-679f46c1b433:STORY,b25244ce-c216-3bb1-bb23-f1dc15a7359c:STORY,493d2140-457b-34c9-8880-bc2d5e27c634:STORY,7692f62b-2e27-3a4f-975d-937d69da5895:STORY,bcd6efe2-9bb7-3699-8518-3ab37d8a5126:STORY,ed7b9959-4d22-3eeb-9cb2-a192dccff189:STORY,80a4f6ea-e3ec-301c-a463-5ef61b45d058:STORY,25292b21-3aa6-39dc-a3db-3b3e128bad87:STORY,81174b76-6bc0-3dac-a17c-3ad6a4bd54ba:STORY,b2ae584f-9f89-3553-92ab-f552f366eff8:STORY,ed960aa8-d851-3880-abfa-cb64972c3365:STORY,013f3a26-06d7-3bb6-8811-ddbc901f9eec:STORY,5be8e09f-a38f-33f2-8c7a-b132c6bb610b:STORY,08bf9f01-05cf-3ec6-80bb-2101a08adc85:STORY,47f6382b-93cb-3a1b-b646-ca5c7e112b1c:STORY,44c0117c-93cc-39ce-a2e0-a65135a3eaf0:STORY,300bf28c-ad14-3ffa-997b-ddca30c87009:STORY,5ae7d8bb-6878-37cf-87f3-2a790ddae64d:STORY,ee662fda-edf7-30a7-840b-e5cd92d065a5:STORY,74931b0b-5d2f-3ff7-ba15-cac585af247d:STORY,6f436bdb-3f70-3803-bf38-af978276bacb:STORY,7ad26b01-4c77-3ca1-9ca2-650f4d662801:STORY,9ca63bdd-11a8-312b-8286-9222c9e81f3a:STORY,70f18cb0-a87e-360e-8ef8-c596000a53f9:STORY,081973d7-6ebd-30ef-97aa-8dbbb8253ba2:STORY,a7d28e54-d4f6-35d1-920f-9db04c00e2f8:STORY,994ab79f-cdbf-34a1-8e93-8c9ed7bb82a7:STORY,7df32d56-ffc0-301d-a5ee-b910583670fd:STORY,301b0abb-17de-35f6-940e-4bd4141ef918:STORY,f0ba7d8d-720b-3142-9d56-fedd361dabf1:STORY,88c55e58-568d-3e58-a21f-67366fc1da36:STORY,ffc04835-c206-33ff-9f64-dcc089cbdc46:STORY,637464cb-46b3-39cf-9b19-9b8323ccf204:STORY,a9733097-b00d-3b9e-beac-7ae367b838eb:STORY,c4b016f4-fc18-36b3-a079-6409219d5c65:STORY,005b1011-7b74-341e-b533-19f52e1def4a:STORY,d2da7f8d-5143-480f-afaa-489ba122f921:STORY,f1ee18b8-e4e4-3632-8edb-547b095c5b9a:STORY,9ab3be9f-83a9-3e06-a4fa-4beb0d314110:STORY,face7dbd-4541-397e-b280-3a9a748910f5:STORY,5e6a30ee-2072-3e75-b943-cca6e4c567f0:STORY,0c7f40dd-44a9-3c51-ac4d-2ccfc7490b3a:STORY,2ac92b15-3bc7-3cf9-bca6-a0b0e7d482c0:STORY,1265b367-e204-3251-94f0-004ec932c48d:STORY,33e6b50f-8cac-3108-a546-28be3a8960aa:STORY,cb30ec70-70bb-3d48-b1f3-fd81d5f02943:STORY,fc600458-e0d9-38fc-9234-3fb878f626d7:STORY,80801724-76a1-36b9-96b1-74940a9da9dc:STORY,0ef62af5-c5b4-3154-9487-f0253325d4db:STORY,fb8693f6-d2eb-33be-bbc9-d81deb0b5429:STORY,2f6d48cd-637e-3886-9521-641df2df312c:STORY,1d4fd9b1-6e9c-396d-ba16-12a598c0a9f3:STORY,105ae3b1-f8bc-3c62-80e5-6ff0506c22ee:STORY,122449e8-b87b-33a5-ae22-63ae3842e91b:STORY,b948e9be-4528-3c7c-b1a7-a2cd0e9e7a94:STORY,0f4ce152-acf8-34cc-af2f-eeebf35001d8:STORY,1283faeb-a5b7-30cb-81ea-5dcec9adf11c:STORY,24cac6ea-206c-3d7b-94a6-e3d45f83db7b:STORY,2bbd95d5-df0f-34a3-882d-90f59a31c437:STORY,0eaf877b-d05b-3387-8f9a-20233273ac46:STORY,f3c061ed-37ca-3153-b875-9d456bd8f919:STORY,9935b348-67a8-3bc4-b0cd-8b132184d698:STORY,970d9c71-3bcd-30a9-ac0b-1c762797dc9b:STORY,758558ed-5483-3092-ad3c-96b4538b84c2:STORY,4936557c-3746-3499-954c-8b82a8aa55e9:STORY,19db7803-978a-3a92-80fc-8825bcb3a05c:STORY,9e74a144-a656-311c-9a06-ef979d52a68a:STORY,8d00f581-d274-3379-8396-d3b706601507:STORY,609b4789-da16-3547-8bcf-e2fd96ed7b1d:STORY,edb87acc-8014-3876-a5b2-ad50741e913f:STORY,994160e1-dc99-3912-9684-3e2bf2ff2d3c:STORY,9d5bc34f-d231-3cfb-8d0b-cc64d3b96cc7:STORY,f6f7f8d8-af45-3e76-b697-8cb9cbc23273:STORY,7a61721c-1b1f-3257-9fd6-6c1ab575f5f9:STORY,3662e412-a9b6-3048-9f9d-571aee7fdb8f:STORY,8cce3923-cb86-32af-9e99-2a0c29319ae0:STORY,2e549703-d54f-3c51-affc-f984db288c9d:STORY,cd928775-c92a-3e4f-b235-0434181cd90e:STORY,e952b2ff-9b68-3af4-98d2-450855d34000:STORY,7b9013f6-13ee-3e93-9443-bddc9cb5b2c6:STORY,600526af-5594-3066-90a0-315666eaec2c:STORY,ebcd56af-5900-3a7f-9c11-d6640d8cd34d:STORY,ba5bf347-87cf-36f3-86a8-2c7f03c3ef03:STORY,956d198b-1eff-3828-94f1-b121947078f9:STORY,cc95c968-320f-3eb4-96f1-886013a80b68:STORY,16d08a9b-61bd-3b0b-822b-0bf460769125:STORY,8340699f-de66-3e56-b3cc-df3413a7bf7f:STORY,47ee38e6-1a70-3246-a358-1a8983051a20:STORY,d2153adb-68d7-3827-aa5a-ae683e340641:STORY,e1cdb42d-9b21-3779-88ee-ef87dc2c3e71:STORY,e43b0db1-d627-3eca-ac03-221067bb04c1:STORY,1fb153a7-eb71-33c7-b606-f53c09cc79ce:STORY,3eaea3d0-c21e-39aa-a42e-ee05b8989302:STORY,d64bd361-d247-3ced-b9eb-f6b87c05dc04:STORY,66393c1d-27f7-3c97-9dd0-86be2c1ff4da:STORY,b7d92045-a11b-383b-adc1-6f1a7d9b460a:STORY,66e980d4-80cd-361d-87a7-a804b7bdd3a3:STORY,e96be844-6cec-438f-a374-3d1ed4a35a7b:STORY,6bf9ba22-5965-3c18-b3a7-0f7d75018516:STORY,655d0819-169c-31f3-8796-37c65c66e2e0:STORY,9a84c7be-6eac-312f-bb4d-75a0a40c7a2e:STORY,be4a8bde-2cb0-352f-a100-fb5ec95e20de:STORY,9f2dca47-24fd-365e-9e31-0100786d630d:STORY,410375c2-78c2-3913-afdb-04dda1f69de0:STORY,f4c5eec9-d164-32d1-9dd0-e0335a90f239:STORY,9ebfd39f-e92e-3588-a6e3-02cc98994fc0:STORY,25f4ada6-f8f0-3bd7-bdae-a10ad7cab7d3:STORY,e4bcf04e-8761-341d-b093-975527bc7735:STORY,551f4726-1abc-3aa6-ad10-0d6ef9758766:STORY,fcd2cd6d-ee61-3869-95ad-3e9ae327db96:STORY"

                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "context": {
        "feature": "adsMigration,canvassOffnet,ccOnMute,disableCommentsMessage,debouncesearch100,deferDarla,ecmaModern,emptyServiceWorker,enable3pConsent,enableCCPAFooter,enableCMP,enableConsentData,enableFeatureTours,enableFinancialsTemplate,enableFreeFinRichSearch,enableGuceJs,enableGuceJsOverlay,enableNavFeatureCue,enableNewResearchInsights,enablePfSummaryForEveryone,enablePremiumSingleCTA,enablePrivacyUpdate,enableRebranding,enableStreamDebounce,enableTheming,enableUpgradeLeafPage,enableVideoURL,enableXrayNcp,enableXrayNcpInModal,enableXrayTickerEntities,enableYahooSans,enableYodleeErrorMsgCriOS,ncpListStream,ncpPortfolioStream,ncpQspStream,ncpStream,ncpStreamIntl,ncpTopicStream,newContentAttribution,newLogo,oathPlayer,optimizeSearch,premium35,relatedVideoFeature,reportReactMarkupDiff,threeAmigos,waferHeader,useNextGenHistory,videoNativePlaylist,sunsetMotif2,enableUserPrefAPI,livecoverage,darlaFirstRenderingVisible,enableAdlite,enableTradeit,enableFeatureBar,enableSearchEnhancement,enableUserSentiment,enableBankrateWidget,enableYodlee,canvassReplies,enablePremiumFinancials,enableInstapage,enableNewResearchFilterMW,showExpiredIdeas,showMorningStar,enableSEOResearchReport,enableSingleRail,enableUpgrade,enableAmexOffer,enableUserInsights,enhanceAddToWL,article2_csn,sponsoredAds,enableStageAds,enableTradeItLinkBrokerSecondaryPromo,enableQspPremiumPromoSmall,clientDelayNone,threeAmigosMabEnabled,threeAmigosAdsEnabledAndStreamIndex0,enableRelatedTickers,enableTasteMaker,enableNotification,enableJSErrorBeacon,financeRightRailA20,enableBrokerCenter,enableYahooPlus,enablePremiumUpsell",
        "bkt": [
            "fdw-MASTonQSP-5",
            "xray-us-finance-desktop-minicard-4"
        ],
        "crumb": "dY6cN.CFKNe",
        "device": "desktop",
        "intl": "us",
        "lang": "en-US",
        "partner": "none",
        "prid": "383okn5gcl0as",
        "region": "US",
        "site": "finance",
        "tz": "America/Los_Angeles",
        "ver": "0.102.4903",
        "ecma": "modern"
    }
})
headers = {
    'Content-Type': 'application/json',
    'Host': 'finance.yahoo.com',
    'Cookie': 'A1=d=AQABBAHmmGACEJ6QlnyFkEl5g3EKkUM5d_8FEgEBBAHMpWCPYdwr0iMA_eMAAAcIAeaYYEM5d_8&S=AQAAAvuEn-AY5ddAHYKd_ydNy1M; A1S=d=AQABBAHmmGACEJ6QlnyFkEl5g3EKkUM5d_8FEgEBBAHMpWCPYdwr0iMA_eMAAAcIAeaYYEM5d_8&S=AQAAAvuEn-AY5ddAHYKd_ydNy1M&j=CCPA; A3=d=AQABBAHmmGACEJ6QlnyFkEl5g3EKkUM5d_8FEgEBBAHMpWCPYdwr0iMA_eMAAAcIAeaYYEM5d_8&S=AQAAAvuEn-AY5ddAHYKd_ydNy1M; B=futpp8dg9hpg1&b=3&s=gm; GUC=AQEBBAFgpcxhj0Ij9QTc; thamba=1; cmp=t=1623867852&j=0; APID=VA7e270503-b383-11eb-82f2-06dfb88c5ace; PRF=t%3DNET%252BSQ%252BAAPL%252BTSLA%252BCOIN%252BSNOW%252BGME%252BCOST%252BAMD%252BCRWD%252BELY%252BAMZN%252BFCX%252BWIT; B=aongqp9gckhbf&b=3&s=33'
}


results = []
response = requests.request("POST", url, headers=headers, data=payload)
results += json.loads(response.text)['g0']['data']['stream_items']


for res in results:
    print(res['title'])
    print(res['url'])
    article = requests.request("GET", res['url'])
    soup = BeautifulSoup(article.content, 'html.parser')
    body = soup.find_all('div', class_='caas-body')[0].find_all('p')
    a = ""
    for p in body:
        a += p.get_text()
    tokens = nltk.word_tokenize(a)
    print(tokens)
    break


def sentiment_analysis(text):
    return 