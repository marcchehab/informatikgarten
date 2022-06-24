import { defineDocumentType, makeSource } from "contentlayer/source-files";
import siteConfig from "./config/siteConfig";
import remarkGfm from "remark-gfm";

const sharedFields = {
  title: { type: "string" },
};

const computedFields = {
  url: {
    type: "string",
    resolve: (post) => post._raw.flattenedPath
  },
};

const Page = defineDocumentType(() => ({
  name: "Page",
  filePathPattern: "**/*.md*",
  contentType: "mdx",
  fields: {
    ...sharedFields,
  },
  computedFields,
}));

const contentLayerExcludeDefaults = ['node_modules', '.git', '.yarn', '.cache', '.next', '.contentlayer', 'package.json', 'tsconfig.json']

export default makeSource({
  contentDirPath: siteConfig.content,
  contentDirExclude: contentLayerExcludeDefaults.concat(['.flowershow']),
  documentTypes: [Page],
  mdx: {
    remarkPlugins: [ remarkGfm ],
    rehypePlugins: []
  }
});