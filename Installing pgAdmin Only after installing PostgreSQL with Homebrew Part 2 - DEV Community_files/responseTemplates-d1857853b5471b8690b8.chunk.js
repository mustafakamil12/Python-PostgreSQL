(window.webpackJsonp=window.webpackJsonp||[]).push([[39],{96:function(e,t,n){"use strict";function s(e,t){var n=t.target.dataset.targetType,s="personal"===n?"moderator":"personal";t.target.classList.toggle("active"),e.getElementsByClassName("".concat(s,"-template-button"))[0].classList.toggle("active"),e.getElementsByClassName("".concat(n,"-responses-container"))[0].classList.toggle("hidden"),e.getElementsByClassName("".concat(s,"-responses-container"))[0].classList.toggle("hidden")}n.r(t);function o(e){var t=e.getElementsByClassName("response-templates-container")[0],n="new_comment"!==e.id&&!e.id.includes("edit_comment"),s=Array.from(t.getElementsByClassName("insert-template-button")),o=Array.from(t.getElementsByClassName("moderator-submit-button"));s.forEach((function(n){n.addEventListener("click",(function(n){var s=n.target.dataset.content,o=e.getElementsByTagName("textarea")[0];(null===o.value||""===o.value||confirm("Are you sure you want to replace your current comment draft?"))&&(o.value=s,o.focus(),t.classList.toggle("hidden"))}))})),o.forEach((function(e){e.addEventListener("click",(function(e){var t,s,o;e.preventDefault(),confirm("\nAre you sure you want to submit this comment as Sloan?\n\nIt will be sent immediately and users will be notified.\n\nMake sure this is the appropriate comment for the situation.\n\nThis action is not reversible.")&&(t=e.target.dataset.responseTemplateId,s=n,o=document.getElementById("comment_commentable_id").value,fetch("/comments/moderator_create",{method:"POST",headers:{Accept:"application/json","X-CSRF-Token":window.csrfToken,"Content-Type":"application/json"},body:JSON.stringify({response_template:{id:t},comment:{body_markdown:"",commentable_id:o,commentable_type:"Article",parent_id:s}})}).then((function(e){return e.json()})).then((function(e){"created"===e.status?window.location.pathname=e.path:"comment already exists"===e.status?alert("This comment already exists."):"error"===e.error&&alert("There was a problem submitting this comment: ".concat(e.status))})))}))}))}function a(e,t){var n,s=document.getElementById(t);"personal_comment"===e?n=s.getElementsByClassName("personal-responses-container")[0]:"mod_comment"===e&&(n=s.getElementsByClassName("moderator-responses-container")[0]),fetch("/response_templates?type_of=".concat(e),{method:"GET",headers:{Accept:"application/json","X-CSRF-Token":window.csrfToken,"Content-Type":"application/json"}}).then((function(e){return e.json()})).then((function(t){s.querySelector("img.loading-img").classList.toggle("hidden"),n.innerHTML=function(e,t){return 0===e.length&&"personal_comment"===t?'\n<div class="mod-response-wrapper mod-response-wrapper-empty">\n  <p>\ud83e\udd14... It looks like you don\'t have any templates yet.</p>\n</div>\n':"personal_comment"===t?e.map((function(e){return'\n          <div class="mod-response-wrapper flex mb-4">\n            <div class="flex-1">\n              <h4>'.concat(e.title,"</h4>\n              <p>").concat(e.content,'</p>\n            </div>\n            <div class="pl-2">\n              <button class="crayons-btn crayons-btn--secondary crayons-btn--s insert-template-button" type="button" data-content="').concat(e.content,'">Insert</button>\n            </div>\n          </div>\n        ')})).join(""):"mod_comment"===t?e.map((function(e){return'\n            <div class="mod-response-wrapper mb-4 flex">\n              <div class="flex-1">\n                <h4>'.concat(e.title,"</h4>\n                <p>").concat(e.content,'</p>\n              </div>\n              <div class="flex flex-nowrap pl-2">\n                <button class="crayons-btn crayons-btn--s crayons-btn--secondary moderator-submit-button" type="submit" data-response-template-id="').concat(e.id,'">Send as Mod</button>\n                <button class="crayons-btn crayons-btn--s crayons-btn--outlined insert-template-button" type="button" data-content="').concat(e.content,'">Insert</button>\n              </div>\n            </div>\n          ')})).join(""):"Error \ud83d\ude1e"}(t,e),document.getElementById("response-templates-data").innerHTML=n.parentElement.innerHTML,o(s)}))}function r(e){var t=e.getElementsByClassName("response-templates-container")[0],n=""!==document.getElementById("response-templates-data").innerHTML;t.classList.toggle("hidden");var r=t.classList.contains("hidden");n&&!r?(!function(e){e.innerHTML=document.getElementById("response-templates-data").innerHTML}(t),o(e)):n||r||function(e){e.querySelector("img.loading-img").classList.toggle("hidden"),a("personal_comment",e.id)}(e),userData().moderator_for_tags.length>0?function(e){var t=e.getElementsByClassName("personal-template-button")[0],n=e.getElementsByClassName("moderator-template-button")[0];t.addEventListener("click",(function(t){s(e,t)})),n.addEventListener("click",(function(t){s(e,t)})),n.classList.remove("hidden"),n.addEventListener("click",(function(){var t=document.getElementById("response-templates-data");""!==t.innerHTML&&0===t.getElementsByClassName("moderator-responses-container")[0].childElementCount&&(e.querySelector("img.loading-img").classList.toggle("hidden"),a("mod_comment",e.id))}),{once:!0})}(e):e.getElementsByClassName("personal-template-button")[0].classList.add("hidden")}function c(e){var t=e.getElementsByClassName("response-templates-button")[0];t&&(t.addEventListener("click",(function(){r(e)})),t.dataset.hasListener="true")}function i(){var e,t,n,s=document.body.dataset.userStatus,o=document.getElementsByClassName("comment-form")[0];document.getElementById("response-templates-data")&&("logged-out"===s&&(null===(n=document.getElementsByClassName("response-templates-button")[0])||void 0===n||n.addEventListener("click",showLoginModal)),o&&"false"===o.getElementsByClassName("response-templates-button")[0].dataset.hasListener&&c(o),e=new MutationObserver((function(e){var t=Array.from(e[0].addedNodes).filter((function(e){return"FORM"===e.nodeName}));t.length>0&&c(t[0])})),(t=document.getElementById("comment-trees-container"))&&e.observe(t,{childList:!0,subtree:!0}),window.addEventListener("beforeunload",(function(){e.disconnect()})),window.InstantClick.on("change",(function(){e.disconnect()})))}window.InstantClick.on("change",(function(){i()})),i()}},[[96,71]]]);
//# sourceMappingURL=responseTemplates-d1857853b5471b8690b8.chunk.js.map