
import re
from mkdocs.structure import pages, files
from mkdocs import config
from mkdocs.plugins import BasePlugin


class TorillicIPAPlugin(BasePlugin):
    def on_page_markdown(self, markdown: str, page: pages.Page, config: config.Config, files: files.File) -> str:
        """
        Parse IPA syntax and add a link to ipa-reader.

        Add IPA like so:
        ```
        /ɪntənæʃᵊnᵊl fəʊnɛtɪk ælfəbɛt/
        ```

        The resulting HTML will be:
        ```
        <a class="ipa" href="https://ipa-reader.xyz?text=ɪntənæʃᵊnᵊl%20fəʊnɛtɪk%20ælfəbɛt>ɪntənæʃᵊnᵊl fəʊnɛtɪk ælfəbɛt</a>
        ```

        Parameters
        ----------
        markdown : str
            Markdown text
        page : pages.Page
            MkDocs page object
        config : config.Config
            MkDocs configutation object
        files : files.File
            MkDocs file object

        Returns
        -------
        str
            Parsed markdown text
        """

        def construct_ipa(match):
            """
            Construct an IPA link from an IPA markdown string.

            Parameters
            ----------
            match : re.Match
                Regex match for the IPA text
            """
            # get IPA from regex match
            bef, ipa, aft = match.groups()
            # make websafe
            websafe = ipa.replace(" ", "%20")

            return f"{bef}<a class='ipa' href='https://ipa-reader.xyz?text={websafe}'>{ipa}</a>{aft}"

        # regex to find IPA strings
        re_ipa = r"(^|\s)\/(.*)\/($|\s)"
        # do substitution
        return re.sub(
            pattern=re_ipa,
            string=markdown, 
            repl=construct_ipa
        )